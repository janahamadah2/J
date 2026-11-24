/* drill-core.js — pure drill logic (no DOM). Inlined into the drill page by
 * build-drill.py and loaded by simulate.js, so the simulations test the exact
 * code the page runs.
 *
 * Progress state S (saved in localStorage and synced to the account):
 *   seq        global answer counter (rest periods are counted in answers)
 *   p[id]      {h: recent results, ls: seq at last answer, lt: time, sid: session,
 *               t: last change, n: answers, sc: last full-question score 0..1,
 *               lp: last answer position (string)}
 *              h characters: R right, W wrong, P partly right, G right but guessed,
 *              r / w single-row practice right / wrong (r never counts toward solid)
 *   stars[id]  {on: 0|1, t}
 *   miss[]     {q, lab, t}  every wrong pick (misconception label when one exists)
 *   lastSid    id of the most recent session started
 */
(function (root) {
  'use strict';
  var H18 = 18 * 3600 * 1000;

  function rng(seed) {
    var a = (seed >>> 0) || 1;
    return function () {
      a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function shuffle(a, r) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(r() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function range(n) { var a = []; for (var i = 0; i < n; i++) a.push(i); return a; }

  function newState() {
    return { v: 1, seq: 0, p: {}, stars: {}, miss: [], pre: { last: null }, tsec: { s: 0, n: 0 },
             lc: {}, ll: -1, lastSid: null, sidN: 0, t: 0 };
  }

  /* ------------------------------------------------------------ data context */
  function makeCtx(DATA) {
    var D = { cfg: DATA.cfg, items: DATA.items, concepts: DATA.concepts || {}, byId: {}, hiUnits: {} };
    DATA.items.forEach(function (it) { D.byId[it.id] = it; });
    (DATA.cfg.high_roi_units || []).forEach(function (u) { D.hiUnits[u] = 1; });
    return D;
  }
  // a question id is "q12" or a single-row variant "q12r3"
  function parseId(qid) {
    var m = /^(q\d+)(?:r(\d+))?$/.exec(qid);
    return m ? { base: m[1], row: m[2] === undefined ? -1 : +m[2] } : { base: qid, row: -1 };
  }
  function itemOf(D, qid) {
    var p = parseId(qid), it = D.byId[p.base];
    if (!it || p.row < 0) return it;
    return { id: qid, base: it.id, row: p.row, u: it.u, t: 'row', k: it.k, lp: it.lp, src: it.src, kind: it.kind,
             q: it.rs[p.row], o: it.o.choices, c: it.c[p.row], w: it.w, x: it.x, m: it.m, parent: it };
  }

  /* ------------------------------------------------------------ status */
  function eff(h) { return (h || '').replace(/r/g, '').replace(/w/g, 'W'); }
  function status(it, rec) {
    if (!rec) return 'new';
    var e = eff(rec.h);
    if (!e) return 'new';
    var last = e.charAt(e.length - 1);
    if (last !== 'R') return 'shaky';
    var need = it.t === 'tf' ? 3 : 2;
    return e.slice(-need) === new Array(need + 1).join('R') ? 'solid' : 'once';
  }
  function trailingMiss(rec) {
    var e = eff(rec && rec.h), n = 0;
    for (var i = e.length - 1; i >= 0 && (e[i] === 'W' || e[i] === 'P'); i--) n++;
    return n;
  }
  function lastIsMiss(rec) { var e = eff(rec && rec.h); var c = e.charAt(e.length - 1); return c === 'W' || c === 'P' || c === 'G'; }
  function isStar(S, id) { var s = S.stars[id]; return !!(s && s.on); }
  function isHi(D, S, it) { return isStar(S, it.id) || !!it.lp || !!D.hiUnits[it.u]; }

  function restLen(D, S, it, rec, n) {
    var e = eff(rec.h), last = e.charAt(e.length - 1);
    if (last === 'W' || last === 'P') {
      return trailingMiss(rec) >= 2 ? clamp(Math.round(0.10 * n), 6, 25) : clamp(Math.round(0.25 * n), 10, 60);
    }
    if (last === 'G') return clamp(Math.round(0.25 * n), 10, 60);
    var b = clamp(Math.round(0.7 * n), 12, 300);
    if (status(it, rec) === 'solid') b = Math.round(b * 1.5);
    if (isHi(D, S, it)) b = clamp(Math.round(0.4 * b), 8, 120);
    return b;
  }
  function isRested(D, S, it, n, now) {
    var rec = S.p[it.id];
    if (!rec || !eff(rec.h)) return true;
    if (now - rec.lt >= H18) return true;
    return (S.seq - rec.ls) >= restLen(D, S, it, rec, n);
  }
  // answered in the previous session and not allowed back yet
  function prevBlocked(D, S, it) {
    var rec = S.p[it.id], blk = S._block !== undefined ? S._block : S.lastSid;
    if (!rec || !blk || rec.sid !== blk) return false;
    return !(isHi(D, S, it) || trailingMiss(rec) >= 2);
  }

  /* ------------------------------------------------------------ pools */
  function unitItems(D, units) {
    var set = {}; units.forEach(function (u) { set[u] = 1; });
    return D.items.filter(function (it) { return set[it.u]; });
  }
  var FILTERS = {
    missed: function (D, S, it) { return status(it, S.p[it.id]) === 'shaky'; },
    starred: function (D, S, it) { return isStar(S, it.id); },
    lp: function (D, S, it) { return !!it.lp; },
    never: function (D, S, it) { return status(it, S.p[it.id]) === 'new'; }
  };
  function pool(D, S, units, filters, overlap) {
    var base = unitItems(D, units), act = Object.keys(FILTERS).filter(function (f) { return filters && filters[f]; });
    if (!act.length) return base.map(function (it) { return it.id; });
    return base.filter(function (it) {
      var hits = act.map(function (f) { return FILTERS[f](D, S, it); });
      return overlap ? hits.every(Boolean) : hits.some(Boolean);
    }).map(function (it) { return it.id; });
  }
  function filterCounts(D, S, units) {
    var base = unitItems(D, units), out = {};
    Object.keys(FILTERS).forEach(function (f) { out[f] = base.filter(function (it) { return FILTERS[f](D, S, it); }).length; });
    return out;
  }

  /* ------------------------------------------------------------ sequencing */
  function tfTruth(it) { return it.t === 'tf' ? (it.c === 0) : null; }
  function tfOK(it, tfh) {
    if (it.t !== 'tf') return true;
    var v = tfTruth(it), n = tfh.length;
    return !(n >= 2 && tfh[n - 1] === v && tfh[n - 2] === v);
  }
  // Order a list so the same topic never comes twice in a row when that is
  // possible, the same format is avoided, and no 3 identical true/false answers
  // run together (three true/false questions back to back with the same answer;
  // any other question in between breaks the run). prev = {u, t, tfh} carries
  // the state across a session; tfh holds true/false/null for the last questions.
  function arrangeSeq(D, ids, r, prev) {
    prev = prev || {};
    var groups = {}, order = [], total = ids.length;
    ids.forEach(function (id) { var it = itemOf(D, id); (groups[it.u] = groups[it.u] || []).push(id); });
    Object.keys(groups).forEach(function (u) { shuffle(groups[u], r); });
    var lastU = prev.u, lastT = prev.t, tfh = (prev.tfh || []).slice(), out = [];
    while (total > 0) {
      var units = Object.keys(groups).filter(function (u) { return groups[u].length; });
      var cand = units.filter(function (u) { return u !== lastU; });
      if (!cand.length) cand = units;
      var maxU = cand[0];
      cand.forEach(function (u) { if (groups[u].length > groups[maxU].length) maxU = u; });
      var pick;
      if (groups[maxU].length * 2 >= total) pick = maxU;
      else {
        var sum = 0; cand.forEach(function (u) { sum += groups[u].length; });
        var x = r() * sum; pick = cand[cand.length - 1];
        for (var i = 0; i < cand.length; i++) { x -= groups[cand[i]].length; if (x < 0) { pick = cand[i]; break; } }
      }
      var hasOK = function (u) { return groups[u].some(function (q) { return tfOK(itemOf(D, q), tfh); }); };
      if (!hasOK(pick)) {
        var alt = cand.filter(hasOK);
        if (!alt.length) alt = units.filter(function (u) { return u !== lastU && hasOK(u); });
        if (alt.length && !(groups[pick].length * 2 > total + 1)) pick = alt[Math.floor(r() * alt.length)];
      }
      var g = groups[pick], j = -1;
      for (var k = 0; k < g.length && j < 0; k++) { var a = itemOf(D, g[k]); if (a.t !== lastT && tfOK(a, tfh)) j = k; }
      for (k = 0; k < g.length && j < 0; k++) { if (tfOK(itemOf(D, g[k]), tfh)) j = k; }
      if (j < 0) j = 0;
      var id = g.splice(j, 1)[0], it = itemOf(D, id);
      out.push(id); total--; lastU = it.u; lastT = it.t;
      tfh.push(tfTruth(it));
    }
    return repairTF(D, out, prev);
  }
  // Moves a true/false item that would make 3 identical answers in a row to the
  // earliest place where it breaks no rule (true/false runs, topic adjacency).
  function tfBad(D, seq, tfh0) {
    var tfh = tfh0.slice();
    for (var i = 0; i < seq.length; i++) {
      var z = itemOf(D, seq[i]);
      if (!tfOK(z, tfh)) return i;
      tfh.push(tfTruth(z));
    }
    return -1;
  }
  function adj(D, seq, prevU) {
    var n = 0, last = prevU;
    seq.forEach(function (q) { var u = itemOf(D, q).u; if (u === last) n++; last = u; });
    return n;
  }
  function repairTF(D, seq, prev) {
    var tfh0 = (prev && prev.tfh) || [], guard = 0, i;
    while ((i = tfBad(D, seq, tfh0)) >= 0 && guard++ < 50) {
      var base = adj(D, seq, prev && prev.u), done = false;
      for (var slack = 0; slack <= 2 && !done; slack++) {
        for (var k = 0; k < seq.length && !done; k++) {
          if (k === i) continue;
          var t = seq.slice(), x = t.splice(i, 1)[0];
          t.splice(k, 0, x);
          var b = tfBad(D, t, tfh0);
          if ((b < 0 || b > i) && adj(D, t, prev && prev.u) <= base + slack) { seq = t; done = true; }
        }
      }
      if (!done) break;
    }
    return seq;
  }

  function info(D, S, it, n, now) {
    var rec = S.p[it.id], st = status(it, rec);
    return { id: it.id, it: it, rec: rec, st: st, hi: isHi(D, S, it), rested: isRested(D, S, it, n, now),
             blocked: prevBlocked(D, S, it), miss: !!rec && st === 'shaky', cons: trailingMiss(rec) >= 2,
             lt: rec ? rec.lt : 0 };
  }

  /* limited session: up to 1/4 rested misses, up to 1/5 rested review checks,
     then never answered (high ROI first-ish), then more rested, then recent. */
  function buildLimited(D, S, ids, N, nTopic, r, now) {
    var all = ids.map(function (id) { return info(D, S, D.byId[id], nTopic, now); });
    var elig = all.filter(function (x) { return !x.blocked; });
    var taken = {}, pick = [], counts = { miss: 0, review: 0, fresh: 0, more: 0, recent: 0, prev: 0 };
    function take(list, max, key) {
      for (var i = 0; i < list.length && max > 0 && pick.length < N; i++) {
        var x = list[i]; if (taken[x.id]) continue;
        taken[x.id] = 1; pick.push(x.id); counts[key]++; max--;
      }
    }
    var misses = elig.filter(function (x) { return x.miss && x.rested; })
      .sort(function (a, b) { return (b.cons - a.cons) || (a.lt - b.lt); });
    var rights = elig.filter(function (x) { return x.rec && !x.miss && x.st !== 'new' && x.rested; })
      .sort(function (a, b) { return (b.hi - a.hi) || (a.lt - b.lt); });
    var fresh = shuffle(elig.filter(function (x) { return x.st === 'new'; }), r)
      .map(function (x) { return { x: x, k: r() - (x.hi ? 0.5 : 0) }; })
      .sort(function (a, b) { return a.k - b.k; }).map(function (o) { return o.x; });
    take(misses, Math.floor(N / 4), 'miss');
    take(rights, Math.floor(N / 5), 'review');
    take(fresh, N, 'fresh');
    take(misses.concat(rights).sort(function (a, b) { return a.lt - b.lt; }), N, 'more');
    var note = null;
    if (pick.length < N) {
      var recent = elig.filter(function (x) { return !taken[x.id]; }).sort(function (a, b) { return a.lt - b.lt; });
      if (recent.length) { take(recent, N, 'recent'); note = 'recent'; }
    }
    if (pick.length < N) {
      var blocked = all.filter(function (x) { return x.blocked && !taken[x.id]; }).sort(function (a, b) { return a.lt - b.lt; });
      if (blocked.length) { take(blocked, N, 'prev'); note = 'prev'; }
    }
    return { ids: arrangeSeq(D, pick, r, { tfh: S.tfh || [] }), counts: counts, note: note };
  }

  function nextEndless(D, S, ids, nTopic, r, now, recent, prev) {
    prev = prev || {};
    var rec5 = {}; (recent || []).slice(-5).forEach(function (q) { rec5[parseId(q).base] = 1; });
    var all = ids.map(function (id) { return info(D, S, D.byId[id], nTopic, now); })
      .filter(function (x) { return !rec5[x.id]; });
    var cand = all.filter(function (x) { return x.rested && !x.blocked; });
    if (!cand.length) cand = all.slice().sort(function (a, b) { return a.lt - b.lt; }).slice(0, 10);
    if (!cand.length) return null;
    var tfh = prev.tfh || [], ws = cand.map(function (x) {
      var w = (x.miss ? 3 : 1) * (x.hi ? 1.5 : 1);
      if (x.it.u === prev.u) w *= 0.15;
      if (x.it.t === prev.t) w *= 0.4;
      if (!tfOK(x.it, tfh)) w *= 0.02;
      return w;
    });
    var sum = ws.reduce(function (a, b) { return a + b; }, 0), y = r() * sum;
    for (var i = 0; i < cand.length; i++) { y -= ws[i]; if (y < 0) return cand[i].id; }
    return cand[cand.length - 1].id;
  }

  var ST_RANK = { shaky: 0, 'new': 1, once: 2, solid: 3 };
  function buildLastPass(D, S, only20, r) {
    var lp = D.items.filter(function (it) { return it.lp; });
    var groups = [[], [], [], []];
    lp.forEach(function (it) { groups[ST_RANK[status(it, S.p[it.id])]].push(it.id); });
    var out = [], prev = { tfh: S.tfh || [] };
    groups.forEach(function (g) {
      var s = arrangeSeq(D, g, r, prev);
      out = out.concat(s);
      var tfh = prev.tfh.slice();
      s.forEach(function (q) { tfh.push(tfTruth(itemOf(D, q))); });
      if (s.length) { var it = itemOf(D, s[s.length - 1]); prev = { u: it.u, t: it.t, tfh: tfh }; }
    });
    return only20 ? out.slice(0, 20) : out;
  }
  function statusCounts(D, S, ids) {
    var c = { solid: 0, once: 0, shaky: 0, 'new': 0 };
    ids.forEach(function (id) { var it = D.byId[id]; c[status(it, S.p[id])]++; });
    return c;
  }

  /* ------------------------------------------------------------ levels and pre-test */
  function lastScore(rec) {
    var e = eff(rec && rec.h); if (!e) return null;
    var c = e.charAt(e.length - 1);
    if (c === 'R' || c === 'G') return 1;
    if (c === 'P') return typeof rec.sc === 'number' ? rec.sc : 0.5;
    return 0;
  }
  function topicLevels(D, S) {
    var out = {};
    D.cfg.units.forEach(function (u) {
      var sc = [];
      D.items.forEach(function (it) { if (it.u === u) { var s = lastScore(S.p[it.id]); if (s !== null) sc.push(s); } });
      if (!sc.length) { out[u] = { pct: null, n: 0, level: null }; return; }
      var pct = Math.round(100 * sc.reduce(function (a, b) { return a + b; }, 0) / sc.length);
      out[u] = { pct: pct, n: sc.length, level: pct >= 80 ? 'Strong' : pct >= 60 ? 'Okay' : 'Weak' };
    });
    return out;
  }
  function buildPretest(D, S, r) {
    var units = D.cfg.units.slice(), k = D.cfg.pretest_per_topic || (units.length > 10 ? 2 : 3);
    var hasStar = {}; D.items.forEach(function (it) { if (isStar(S, it.id)) hasStar[it.u] = 1; });
    units.sort(function (a, b) {
      return ((D.hiUnits[b] ? 2 : 0) + (hasStar[b] ? 1 : 0)) - ((D.hiUnits[a] ? 2 : 0) + (hasStar[a] ? 1 : 0))
        || D.cfg.units.indexOf(a) - D.cfg.units.indexOf(b);
    });
    var picks = {};
    units.forEach(function (u) {
      var cand = shuffle(D.items.filter(function (it) { return it.u === u && !it.lp; }), r)
        .sort(function (a, b) {
          return (isStar(S, b.id) - isStar(S, a.id)) ||
                 ((status(a, S.p[a.id]) === 'new' ? 0 : 1) - (status(b, S.p[b.id]) === 'new' ? 0 : 1));
        });
      var chosen = [], types = {};
      var cons = {};
      cand.forEach(function (it) { if (chosen.length < k && !types[it.t] && !cons[it.k]) { chosen.push(it.id); types[it.t] = 1; cons[it.k] = 1; } });
      cand.forEach(function (it) { if (chosen.length < k && chosen.indexOf(it.id) < 0 && !cons[it.k]) { chosen.push(it.id); cons[it.k] = 1; } });
      cand.forEach(function (it) { if (chosen.length < k && chosen.indexOf(it.id) < 0) chosen.push(it.id); });
      picks[u] = chosen;
    });
    var out = [];
    for (var i = 0; i < k; i++) units.forEach(function (u) { if (picks[u][i]) out.push(picks[u][i]); });
    var tfh = (S.tfh || []).slice(), bad = false;
    out.forEach(function (q) { var z = D.byId[q]; if (!tfOK(z, tfh)) bad = true; tfh.push(tfTruth(z)); });
    return bad ? arrangeSeq(D, out, r, { tfh: S.tfh || [] }) : out;
  }

  /* ------------------------------------------------------------ timed mixed plan */
  function avgSec(S) { return S.tsec && S.tsec.n >= 3 ? S.tsec.s / S.tsec.n : 45; }
  function buildTimed(D, S, units, minutes, r, now) {
    var avg = avgSec(S), count = Math.max(5, Math.floor(minutes * 60 / avg));
    var items = unitItems(D, units), nTopic = items.length;
    var inf = items.map(function (it) { return info(D, S, it, nTopic, now); }).filter(function (x) { return !x.blocked; });
    count = Math.min(count, inf.length);
    var lv = topicLevels(D, S), shaky = {}, tot = {};
    inf.forEach(function (x) { tot[x.it.u] = (tot[x.it.u] || 0) + 1; if (x.miss) shaky[x.it.u] = (shaky[x.it.u] || 0) + 1; });
    function weakScore(u) {
      var p = lv[u] && lv[u].pct !== null ? lv[u].pct : 70;
      return p - 40 * ((shaky[u] || 0) / (tot[u] || 1));
    }
    var ranked = units.filter(function (u) { return tot[u]; }).sort(function (a, b) { return weakScore(a) - weakScore(b); });
    var weak = ranked.filter(function (u) { return (lv[u] && lv[u].level && lv[u].level !== 'Strong') || shaky[u]; }).slice(0, 3);
    if (weak.length < Math.min(2, ranked.length)) weak = ranked.slice(0, Math.min(2, ranked.length));
    var cap = units.length > 1 ? Math.ceil(count / 2) : count, perU = {}, taken = {}, pick = [], mix = { weak: 0, review: 0, fresh: 0, fill: 0 };
    function ok(x) { return !taken[x.id] && (perU[x.it.u] || 0) < cap; }
    function add(x, key) { taken[x.id] = 1; perU[x.it.u] = (perU[x.it.u] || 0) + 1; pick.push(x.id); mix[key]++; }
    var nW = Math.round(0.5 * count), nR = Math.round(0.3 * count), nN = count - nW - nR;
    // weak topics: shaky first, then never answered, then right once, then the rest; spread round-robin
    var wl = {};
    weak.forEach(function (u) {
      wl[u] = shuffle(inf.filter(function (x) { return x.it.u === u; }), r).sort(function (a, b) {
        function rank(x) { return x.miss ? (x.rested ? 0 : 1) : x.st === 'new' ? 2 : x.st === 'once' ? 3 : x.rested ? 4 : 5; }
        return rank(a) - rank(b);
      });
    });
    var guard = 0;
    while (mix.weak < nW && guard++ < 5000) {
      var moved = false;
      weak.forEach(function (u) {
        if (mix.weak >= nW) return;
        while (wl[u].length && !ok(wl[u][0])) wl[u].shift();
        if (wl[u].length) { add(wl[u].shift(), 'weak'); moved = true; }
      });
      if (!moved) break;
    }
    var review = inf.filter(function (x) { return x.rested && x.rec && x.st !== 'new'; })
      .sort(function (a, b) { return (b.miss - a.miss) || (b.cons - a.cons) || (b.hi - a.hi) || (a.lt - b.lt); });
    review.forEach(function (x) { if (mix.review < nR && ok(x)) add(x, 'review'); });
    var fresh = shuffle(inf.filter(function (x) { return x.st === 'new' || x.st === 'once'; }), r)
      .sort(function (a, b) { return (a.st === 'new' ? 0 : 1) - (b.st === 'new' ? 0 : 1); });
    fresh.forEach(function (x) { if (mix.fresh < nN && ok(x)) add(x, 'fresh'); });
    if (pick.length < count) {
      var rest = inf.filter(function (x) { return !taken[x.id]; }).sort(function (a, b) { return (b.rested - a.rested) || (a.lt - b.lt); });
      rest.forEach(function (x) { if (pick.length < count && ok(x)) add(x, 'fill'); });
    }
    return { ids: arrangeSeq(D, pick, r, { tfh: S.tfh || [] }), mix: mix, weak: weak, avg: avg, count: pick.length };
  }

  /* ------------------------------------------------------------ fix my misses */
  function conceptMembers(D, cid) {
    var c = D.concepts[cid]; if (!c) return [];
    var out = c.items.slice();
    c.items.forEach(function (id) { var it = D.byId[id]; if (it.t === 'cloze' && it.rs) Object.keys(it.rs).forEach(function (k) { out.push(id + 'r' + k); }); });
    return out;
  }
  function followUp(D, S, missedId, used, r) {
    var it = itemOf(D, missedId), cid = it && it.k; if (!cid) return null;
    var base = parseId(missedId).base, usedB = {};
    Object.keys(used).forEach(function (q) { usedB[q] = 1; usedB[parseId(q).base] = 1; });
    var cand = conceptMembers(D, cid).filter(function (q) { var b = parseId(q).base; return b !== base && !usedB[q] && !usedB[b]; });
    if (!cand.length) return null;
    var full = cand.filter(function (q) { return parseId(q).row < 0; });
    var list = full.length ? full : cand;
    return list[Math.floor(r() * list.length)];
  }

  /* ------------------------------------------------------------ option arrangement */
  function nOpts(it) { return it.t === 'tf' ? 2 : it.o.length; }
  function arrange(D, S, qid, r) {
    var it = itemOf(D, qid), rec = S.p[parseId(qid).base] || {}, t = it.t;
    if (t === 'tf') return { perm: [0, 1] };
    if (it.num) return { perm: null };
    if (t === 'mc' || t === 'fill' || t === 'row') {
      var n = it.o.length, key = 'n' + n, lc = S.lc[key] = S.lc[key] || range(n).map(function () { return 0; });
      var allowed = range(n).filter(function (k) { return k !== S.ll && String(k) !== String(rec.lp); });
      if (!allowed.length) allowed = range(n).filter(function (k) { return k !== S.ll; });
      var min = Math.min.apply(null, allowed.map(function (k) { return lc[k]; }));
      var best = allowed.filter(function (k) { return lc[k] === min; });
      var target = best[Math.floor(r() * best.length)];
      var others = shuffle(range(n).filter(function (k) { return k !== it.c; }), r), perm = [];
      for (var i = 0, j = 0; i < n; i++) perm.push(i === target ? it.c : others[j++]);
      lc[target]++; S.ll = target;
      return { perm: perm, pos: String(target) };
    }
    if (t === 'sata') {
      var p, sig, tries = 0;
      do { p = shuffle(range(it.o.length), r); sig = p.map(function (o, i) { return it.c.indexOf(o) >= 0 ? i : -1; }).filter(function (x) { return x >= 0; }).join(','); }
      while (sig === rec.lp && tries++ < 12);
      return { perm: p, pos: sig };
    }
    if (t === 'order') {
      var q, tries2 = 0;
      do { q = shuffle(range(it.o.length), r); } while ((q.join() === range(it.o.length).join() || q.join() === rec.lp) && tries2++ < 20);
      return { perm: q, pos: q.join() };
    }
    if (t === 'cloze') {
      var ch = it.o.choices.length, cp, tries3 = 0, posSig;
      do {
        cp = shuffle(range(ch), r);
        var pos = it.c.map(function (c) { return cp.indexOf(c); });
        posSig = pos.join(',');
        var allSame = pos.every(function (x) { return x === pos[0]; });
      } while ((allSame || posSig === rec.lp) && tries3++ < 20);
      return { perm: cp, pos: posSig };
    }
    if (t === 'blanks') {
      var bp, tries4 = 0, bs;
      do {
        bp = it.o.map(function (opts) { return shuffle(range(opts.length), r); });
        var bpos = bp.map(function (pp, b) { return pp.indexOf(it.c[b]); });
        bs = bpos.join(',');
        var same = bpos.length > 1 && bpos.every(function (x) { return x === bpos[0]; });
      } while ((same || bs === rec.lp) && tries4++ < 30);
      return { perm: bp, pos: bs };
    }
    return { perm: null };
  }

  /* ------------------------------------------------------------ grading */
  function parseNum(s) {
    s = String(s || '').trim().replace(/,/g, '').replace(/[a-z%/]+\s*$/i, function (m) { return /\d\/\d/.test(m) ? m : ''; }).trim();
    var m;
    if ((m = /^(-?\d+)\s+(\d+)\/(\d+)$/.exec(s))) return +m[1] + (+m[2]) / (+m[3]);
    if ((m = /^(-?\d+)\/(\d+)$/.exec(s))) return (+m[1]) / (+m[2]);
    if (/^-?(\d+\.?\d*|\.\d+)$/.test(s)) return parseFloat(s);
    return NaN;
  }
  function grade(D, qid, perm, pick) {
    var it = itemOf(D, qid), t = it.t;
    if (it.num) {
      var raw = String(pick || '').trim(), v = parseNum(raw), ans = it.num.answer;
      var okv = !isNaN(v) && Math.abs(v - ans) <= 1e-6 * Math.max(1, Math.abs(ans));
      var notes = [];
      if (/^\.\d/.test(raw)) notes.push('Leading zero missing: write 0' + raw + ', never ' + raw + '.');
      if (/\.\d*0$/.test(raw) && /\./.test(raw)) notes.push('Trailing zero: write ' + String(parseFloat(raw)) + ', not ' + raw + '.');
      var near = null;
      if (!okv && it.num.near) Object.keys(it.num.near).forEach(function (k) { if (!isNaN(v) && Math.abs(parseNum(k) - v) <= 1e-6 * Math.max(1, Math.abs(v))) near = it.num.near[k]; });
      var acc = null; if (okv && it.num.accept && it.num.accept[raw]) acc = it.num.accept[raw];
      return { sc: okv ? 1 : 0, full: okv, max: 1, right: okv ? 1 : 0, wrong: okv ? 0 : 1, notes: notes, near: near, accept: acc, value: v };
    }
    if (t === 'mc' || t === 'fill' || t === 'row' || t === 'tf') {
      var o = pick === null || pick === undefined || pick < 0 ? -1 : perm[pick];
      var f = o === it.c;
      return { sc: f ? 1 : 0, full: f, max: 1, right: f ? 1 : 0, wrong: f ? 0 : 1, orig: o };
    }
    if (t === 'sata') {
      var origs = (pick || []).map(function (d) { return perm[d]; });
      var right = origs.filter(function (o) { return it.c.indexOf(o) >= 0; }).length, wrong = origs.length - right;
      var score = Math.max(0, right - wrong);
      return { sc: score / it.c.length, full: right === it.c.length && wrong === 0, max: it.c.length, right: right, wrong: wrong, score: score, origs: origs };
    }
    if (t === 'order') {
      var seq = pick || [], fo = seq.length === it.o.length && seq.every(function (x, i) { return x === i; });
      var inPlace = seq.filter(function (x, i) { return x === i; }).length;
      return { sc: fo ? 1 : 0, full: fo, max: 1, right: fo ? 1 : 0, wrong: fo ? 0 : 1, inPlace: inPlace };
    }
    if (t === 'cloze' || t === 'blanks') {
      var rows = it.c.length, okr = 0, origs2 = [];
      for (var i = 0; i < rows; i++) {
        var d = pick && pick[i] !== undefined ? pick[i] : -1;
        var oo = d < 0 ? -1 : (t === 'cloze' ? perm[d] : perm[i][d]);
        origs2.push(oo); if (oo === it.c[i]) okr++;
      }
      return { sc: okr / rows, full: okr === rows, max: rows, right: okr, wrong: rows - okr, score: okr, origs: origs2 };
    }
    return { sc: 0, full: false, max: 1, right: 0, wrong: 1 };
  }
  function missLabels(D, qid, res) {
    var it = itemOf(D, qid), m = it.m || {}, out = [];
    if (it.num) return out;
    if (it.t === 'mc' || it.t === 'fill' || it.t === 'tf' || it.t === 'row') { if (m[res.orig]) out.push(m[res.orig]); }
    else if (it.t === 'sata') (res.origs || []).forEach(function (o) { if (it.c.indexOf(o) < 0 && m[o]) out.push(m[o]); });
    else if (it.t === 'cloze') (res.origs || []).forEach(function (o, i) { if (o >= 0 && o !== it.c[i] && m[o]) out.push(m[o]); });
    else if (it.t === 'blanks') (res.origs || []).forEach(function (o, i) { var k = i + ':' + o; if (o >= 0 && o !== it.c[i] && m[k]) out.push(m[k]); });
    return out;
  }

  /* ------------------------------------------------------------ recording */
  function record(D, S, qid, res, sid, now, secs, pos) {
    var p = parseId(qid), rec = S.p[p.base] = S.p[p.base] || { h: '', ls: 0, lt: 0, sid: null, t: 0, n: 0 };
    var ch = p.row >= 0 ? (res.full ? 'r' : 'w') : (res.full ? 'R' : (res.sc > 0 ? 'P' : 'W'));
    rec.h = (rec.h + ch).slice(-12);
    S.seq++; rec.ls = S.seq; rec.lt = now; rec.sid = sid; rec.t = now; rec.n = (rec.n || 0) + 1;
    if (p.row < 0) rec.sc = Math.round(res.sc * 100) / 100;
    var itm = itemOf(D, qid);
    if (itm) S.tfh = (S.tfh || []).concat([tfTruth(itm)]).slice(-2);
    if (pos !== undefined && pos !== null) rec.lp = pos;
    if (secs > 1 && secs < 600) { S.tsec.s += secs; S.tsec.n++; }
    if (!res.full) {
      var labs = missLabels(D, qid, res);
      S.miss.push({ q: qid, lab: labs.join('; '), t: now });
      if (S.miss.length > 400) S.miss = S.miss.slice(-400);
    }
    S.t = now;
    return rec;
  }
  function markGuessed(S, qid, now) {
    var rec = S.p[parseId(qid).base];
    if (rec && /R$/.test(rec.h)) { rec.h = rec.h.slice(0, -1) + 'G'; rec.t = now; }
  }

  /* ------------------------------------------------------------ merge (sync) */
  function merge(A, B) {
    if (!B) return A;
    var out = JSON.parse(JSON.stringify(A));
    Object.keys(B.p || {}).forEach(function (id) {
      var a = out.p[id], b = B.p[id];
      if (!a || (b.lt || 0) > (a.lt || 0) || ((b.lt || 0) === (a.lt || 0) && (b.t || 0) > (a.t || 0))) out.p[id] = b;
    });
    Object.keys(B.stars || {}).forEach(function (id) {
      var a = out.stars[id], b = B.stars[id];
      if (!a || (b.t || 0) > (a.t || 0)) out.stars[id] = b;
    });
    var seen = {}, mm = [];
    (out.miss || []).concat(B.miss || []).forEach(function (m) { var k = m.q + '@' + m.t; if (!seen[k]) { seen[k] = 1; mm.push(m); } });
    out.miss = mm.sort(function (a, b) { return a.t - b.t; }).slice(-400);
    if (B.pre && B.pre.last && (!out.pre.last || B.pre.last.t > out.pre.last.t)) out.pre.last = B.pre.last;
    out.seq = Math.max(out.seq || 0, B.seq || 0);
    if (B.tsec && B.tsec.n > (out.tsec.n || 0)) out.tsec = B.tsec;
    if ((B.sidN || 0) > (out.sidN || 0)) { out.sidN = B.sidN; }
    if ((B.t || 0) > (out.t || 0)) { out.lastSid = B.lastSid || out.lastSid; out.t = B.t; }
    return out;
  }

  var Core = { rng: rng, shuffle: shuffle, clamp: clamp, newState: newState, makeCtx: makeCtx, parseId: parseId, itemOf: itemOf,
    eff: eff, status: status, trailingMiss: trailingMiss, lastIsMiss: lastIsMiss, isHi: isHi, isStar: isStar, restLen: restLen,
    isRested: isRested, prevBlocked: prevBlocked, unitItems: unitItems, pool: pool, filterCounts: filterCounts,
    arrangeSeq: arrangeSeq, buildLimited: buildLimited, nextEndless: nextEndless, buildLastPass: buildLastPass,
    statusCounts: statusCounts, topicLevels: topicLevels, buildPretest: buildPretest, buildTimed: buildTimed, avgSec: avgSec,
    conceptMembers: conceptMembers, followUp: followUp, arrange: arrange, parseNum: parseNum, grade: grade,
    missLabels: missLabels, record: record, markGuessed: markGuessed, merge: merge, tfOK: tfOK, H18: H18 };
  if (typeof module !== 'undefined' && module.exports) module.exports = Core; else root.Core = Core;
})(this);
