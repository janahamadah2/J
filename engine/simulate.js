// simulate.js — checks the drill's scheduling with the exact core the page runs.
//   node engine/simulate.js dist/cvs-mid2-drill.data.json
const fs = require('fs');
const Core = require('./drill-core.js');
const DATA = JSON.parse(fs.readFileSync(process.argv[2] || 'dist/cvs-mid2-drill.data.json', 'utf8'));
const D = Core.makeCtx(DATA), UNITS = DATA.cfg.units;
const r = Core.rng(12345);
let fails = 0;
function check(ok, msg) { console.log((ok ? '  ok   ' : '  FAIL ') + msg); if (!ok) fails++; }
const isHiRec = (S, id) => Core.isHi(D, S, D.byId[id]);

// answer one question like a learner who is right 65% of the time
let clock = Date.now();
function answer(S, q, sid, pRight) {
  const a = Core.arrange(D, S, q, r), it = Core.itemOf(D, q);
  let pick;
  const right = r() < pRight;
  if (it.num) pick = right ? String(it.num.answer) : '999';
  else if (['mc', 'fill', 'row', 'tf'].includes(it.t)) {
    const n = it.t === 'tf' ? 2 : a.perm.length, d = a.perm.indexOf(it.c);
    pick = right ? d : (d + 1) % n;
  } else if (it.t === 'sata') pick = right ? it.c.map(c => a.perm.indexOf(c)) : [a.perm.indexOf(it.c[0]), a.perm.findIndex(o => !it.c.includes(o))];
  else if (it.t === 'order') pick = right ? it.o.map((_, i) => i) : it.o.map((_, i) => i).reverse();
  else if (it.t === 'cloze') pick = it.c.map((c, i) => right || i ? a.perm.indexOf(c) : (a.perm.indexOf(c) + 1) % a.perm.length);
  else if (it.t === 'blanks') pick = it.c.map((c, b) => right || b ? a.perm[b].indexOf(c) : (a.perm[b].indexOf(c) + 1) % a.perm[b].length);
  const res = Core.grade(D, q, a.perm, pick);
  clock += 40000;
  Core.record(D, S, q, res, sid, clock, 40, a.pos);
  return { a, res, it };
}

// 1. answer letters and true/false balance ------------------------------------
console.log('\n1. Answer positions over 6000 questions (mixed all-topic sessions)');
{
  const S = Core.newState(), letters = {}, tfPerUnit = {}, seq = [];
  let prevLetter = -1, sameAsPrev = 0, mcCount = 0, sameAsLastTime = 0, comeBacks = 0;
  const lastPos = {};
  let sid = 0;
  while (seq.length < 6000) {
    S.lastSid = 's' + (++sid);
    const ids = Core.pool(D, S, UNITS, {}, false);
    const plan = Core.buildLimited(D, S, ids, 40, ids.length, r, clock + sid * 86400000);
    clock += 86400000;
    for (const q of plan.ids) {
      const { a, it } = answer(S, q, S.lastSid, 0.65);
      seq.push(it);
      if (['mc', 'fill', 'row'].includes(it.t) && !it.num) {
        const L = 'ABCDE'[+a.pos]; letters[a.perm.length] = letters[a.perm.length] || {};
        letters[a.perm.length][L] = (letters[a.perm.length][L] || 0) + 1; mcCount++;
        if (+a.pos === prevLetter) sameAsPrev++;
        if (lastPos[q] !== undefined) { comeBacks++; if (lastPos[q] === a.pos) sameAsLastTime++; }
        lastPos[q] = a.pos; prevLetter = +a.pos;
      }
      if (it.t === 'tf') { tfPerUnit[it.u] = tfPerUnit[it.u] || []; tfPerUnit[it.u].push(it.c === 0); }
    }
  }
  Object.keys(letters).forEach(n => {
    const t = Object.values(letters[n]).reduce((x, y) => x + y, 0);
    console.log('  ' + n + '-option questions (' + t + '): ' + Object.keys(letters[n]).sort().map(L => L + ' ' + (100 * letters[n][L] / t).toFixed(1) + '%').join(', '));
  });
  check(sameAsPrev === 0, 'correct letter never the same as the previous question (' + sameAsPrev + ' repeats in ' + mcCount + ')');
  check(sameAsLastTime === 0, 'a returning question never keeps its answer spot (' + sameAsLastTime + ' of ' + comeBacks + ' returns)');
  // true/false streaks as asked in sequence
  let streak = 1, longest = 1, prev = null;
  seq.forEach(it => { const v = it.t === 'tf' ? it.c === 0 : null; streak = v !== null && v === prev ? streak + 1 : 1; if (v !== null) longest = Math.max(longest, streak); prev = v; });
  console.log('  true/false items in the bank, percent true per topic:');
  UNITS.forEach(u => {
    const bank = D.items.filter(it => it.u === u && it.t === 'tf'), tr = bank.filter(it => it.c === 0).length;
    const asked = tfPerUnit[u] || [];
    console.log('    ' + u.padEnd(13) + ' bank ' + tr + '/' + bank.length + ' true (' + Math.round(100 * tr / bank.length) + '%), asked ' + asked.length + ' times, ' + Math.round(100 * asked.filter(Boolean).length / (asked.length || 1)) + '% true');
  });
  check(longest <= 2, 'longest run of back-to-back true/false questions with the same answer: ' + longest);
}

// 2. sessions in a row --------------------------------------------------------
console.log('\n2. Twelve sessions in a row, mixing single topics and all topics');
{
  const S = Core.newState();
  // some history so misses and solid ones exist
  const plan = [['all', 20], ['Physiology', 10], ['all', 20], ['Pathology', 20], ['Pathology', 10], ['all', 40],
                ['Anatomy', 10], ['all', 20], ['Pharmacology', 20], ['all', 20], ['Microbiology', 10], ['all', 40]];
  let prevIds = new Set(), totalBack = 0, badBack = 0;
  plan.forEach(([sel, N], i) => {
    const units = sel === 'all' ? UNITS : [sel];
    const ids = Core.pool(D, S, units, {}, false);
    const built = Core.buildLimited(D, S, ids, N, ids.length, r, clock);
    const back = built.ids.filter(q => prevIds.has(q));
    const okBack = back.filter(q => isHiRec(S, q) || Core.trailingMiss(S.p[q]) >= 2);
    totalBack += back.length; badBack += back.length - okBack.length;
    S.lastSid = 'sess' + i;
    built.ids.forEach(q => answer(S, q, S.lastSid, 0.65));
    clock += 3 * 3600000; // 3 hours between sessions
    console.log('  session ' + String(i + 1).padStart(2) + ' (' + sel.padEnd(12) + ' ' + String(N).padStart(2) + '): ' + built.ids.length + ' asked, ' + back.length + ' from previous session' +
      (back.length ? ' (all high ROI or consistently missed: ' + (okBack.length === back.length ? 'yes' : 'NO') + ')' : '') +
      ' | mix ' + JSON.stringify(built.counts));
    prevIds = new Set(built.ids);
  });
  check(badBack === 0, totalBack + ' questions came back from the previous session; ' + badBack + ' were neither high ROI nor consistently missed');
}

// 3. pre-test -------------------------------------------------------------------
console.log('\n3. Pre-test');
{
  const S = Core.newState(), pre = Core.buildPretest(D, S, r);
  const per = {}; pre.forEach(q => { const u = D.byId[q].u; per[u] = (per[u] || 0) + 1; });
  const k = UNITS.length > 10 ? 2 : 3;
  check(UNITS.every(u => per[u] === k), 'questions per topic: ' + UNITS.map(u => u + ' ' + (per[u] || 0)).join(', '));
  check(pre.every(q => !D.byId[q].lp), 'last-pass questions in the pre-test: ' + pre.filter(q => D.byId[q].lp).length);
  let rep = 0; pre.forEach((q, i) => { if (i && D.byId[q].u === D.byId[pre[i - 1]].u) rep++; });
  check(rep === 0, 'same topic twice in a row: ' + rep);
  const fm = {}; pre.forEach(q => { const t = D.byId[q].num ? 'numeric' : D.byId[q].t; fm[t] = (fm[t] || 0) + 1; });
  console.log('  formats: ' + JSON.stringify(fm));
  S.lastSid = 'pre';
  pre.forEach(q => answer(S, q, 'pre', 0.6));
  const lv = Core.topicLevels(D, S);
  check(UNITS.every(u => lv[u].level), 'ran all ' + pre.length + ' questions and saved a level for every topic: ' + UNITS.map(u => u + ' ' + lv[u].level + ' ' + lv[u].pct + '%').join(', '));
}

// 4. timed plans ------------------------------------------------------------------
console.log('\n4. Timed mixed plans with saved misses');
{
  const S = Core.newState();
  // history: two all-topic sessions, Physiology and Pharmacology answered poorly
  for (let s = 0; s < 3; s++) {
    S.lastSid = 'h' + s;
    const ids = Core.pool(D, S, UNITS, {}, false);
    Core.buildLimited(D, S, ids, 40, ids.length, r, clock).ids.forEach(q => {
      const u = D.byId[q].u;
      answer(S, q, S.lastSid, u === 'Physiology' || u === 'Pharmacology' ? 0.3 : 0.8);
    });
    clock += 20 * 3600000;
  }
  [30, 45].forEach(mins => {
    const t = Core.buildTimed(D, S, UNITS, mins, r, clock), c = t.count;
    let rep = 0; t.ids.forEach((q, i) => { if (i && D.byId[q].u === D.byId[t.ids[i - 1]].u) rep++; });
    const pct = k => Math.round(100 * t.mix[k] / c);
    console.log('  ' + mins + ' min at ' + Math.round(t.avg) + ' s/question: ' + c + ' questions; weak topics ' + t.weak.join(', ') +
      '; mix weak ' + t.mix.weak + ' (' + pct('weak') + '%), review ' + t.mix.review + ' (' + pct('review') + '%), new/right-once ' + t.mix.fresh + ' (' + pct('fresh') + '%)' + (t.mix.fill ? ', fill ' + t.mix.fill : ''));
    check(rep === 0, mins + '-min plan: same topic twice in a row ' + rep + ' times');
    check(Math.abs(pct('weak') - 50) <= 5 && Math.abs(pct('review') - 30) <= 5 && Math.abs(pct('fresh') - 20) <= 5, mins + '-min plan mix is about 50/30/20');
  });
}

console.log('\n' + (fails ? fails + ' CHECK(S) FAILED' : 'All checks passed.'));
process.exit(fails ? 1 : 0);
