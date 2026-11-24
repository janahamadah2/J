#!/usr/bin/env python3
"""Build a finished drill page from a config and its content files.

    python3 engine/build-drill.py exams/cvs-mid2/config-cvs-mid2.json

A question is a tuple (topic, type, question, options, correct, why).
Types: mc, sata, cloze (matching table), fill (word bank), order, tf, blanks.
Content files (every key is the exact question text):
  EXPLAIN   = {question: {wrong option: "why it is wrong"}}
  LAST_PASS = [question, ...]
  CONCEPTS  = [{"id", "unit", "title", "points", "source", "items": [question, ...]}]
  MISC      = {question: {wrong option: "short misconception label"}}
  ROW_STEMS = {matching question: {row prompt: "one-section question for that row"}}
  NUMERIC   = {question: {"answer", "unit", "accept": {}, "near": {}}}
  WHY       = {question: "full repaired rationale"}
  OVERRIDES = {question: {"question"|"options"|"correct"|"why"|"topic": value}}
The builder refuses to build, with a clear message, when anything does not match.
"""
import html
import importlib.util
import json
import os
import re
import sys

ENGINE = os.path.dirname(os.path.abspath(__file__))
TYPES = {"mc", "sata", "cloze", "fill", "order", "tf", "blanks"}
_mods = {}


def die(msg):
    sys.exit("build-drill: REFUSED - " + msg)


def load(cfg_dir, rel):
    path = os.path.normpath(os.path.join(cfg_dir, rel))
    if path not in _mods:
        if not os.path.exists(path):
            die("content file not found: %s" % rel)
        sys.path.insert(0, os.path.dirname(path))
        spec = importlib.util.spec_from_file_location("content_%d" % len(_mods), path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.path.pop(0)
        _mods[path] = mod
    return _mods[path]


def gather(cfg, cfg_dir, field, name, kind):
    out = [] if kind == "list" else {}
    for rel in cfg.get(field) or []:
        val = getattr(load(cfg_dir, rel), name, None)
        if val is None:
            continue
        if kind == "list":
            out.extend(val)
        else:
            for k, v in val.items():
                if isinstance(v, dict) and isinstance(out.get(k), dict):
                    out[k].update(v)
                else:
                    out[k] = v
    return out


def norm(text):
    t = re.sub(r"<[^>]+>", " ", text)
    t = html.unescape(t).replace("[[", "").replace("]]", "")
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", t).strip().lower()


def deck_items(path, unit):
    """Quizlet export (front TAB back) -> term questions with look-alike wrong options
    (shared root or suffix with the right term, never random other cards)."""
    cards = [l.rstrip("\n").split("\t", 1) for l in open(path, encoding="utf-8") if "\t" in l]
    terms = [c[0].strip() for c in cards]
    out = []
    for front, back in cards:
        front = front.strip()
        def alike(t):
            a, b = t.lower(), front.lower()
            return t != front and (a[:4] == b[:4] or a[-4:] == b[-4:])
        wrongs = [t for t in terms if alike(t)][:4]
        if len(wrongs) < 2:
            continue
        q = "A client's record describes: %s. Which term should the nurse use?" % back.strip()
        out.append((unit, "mc", q, [front] + wrongs, 0, "%s means %s. (Quizlet deck)" % (front, back.strip())))
    return out


def kind_of(q, typ, numeric):
    s = q.lower()
    if numeric:
        return "Calculation"
    if re.search(r"\bfirst\b|priority|most closely|immediate", s):
        return "Priority / first action"
    if re.search(r"teach|statement by|indicates|explain|asks|response", s):
        return "Teaching and statements"
    if re.search(r"interpret|identify|recogni|expect|suspect|anticipate|finding|consistent", s):
        return "Recognize and interpret"
    return "Apply a fact"


def build(cfg_path):
    cfg_dir = os.path.dirname(os.path.abspath(cfg_path))
    cfg = json.load(open(cfg_path))
    units = cfg["units"]

    # ---------------------------------------------------------------- items
    raw = []
    for rel in cfg["items_module"]:
        raw.extend(getattr(load(cfg_dir, rel), "ITEMS"))
    if cfg.get("deck"):
        raw.extend(deck_items(os.path.join(cfg_dir, cfg["deck"]["path"]), cfg["deck"]["unit"]))
    overrides = gather(cfg, cfg_dir, "item_overrides", "OVERRIDES", "dict")
    overrides.update(gather(cfg, cfg_dir, "deck_overrides", "OVERRIDES", "dict"))
    qtext = [r[2] for r in raw]
    for k in overrides:
        n = qtext.count(k)
        if n != 1:
            die("override matches %d questions: %r" % (n, k[:90]))
    items, seen = [], {}
    for idx, (topic, typ, q, opts, correct, why) in enumerate(raw):
        ov = overrides.get(q, {})
        topic, q2 = ov.get("topic", topic), ov.get("question", q)
        opts, correct, why = ov.get("options", opts), ov.get("correct", correct), ov.get("why", why)
        where = "question %d (%s): %r" % (idx, topic, q2[:70])
        if topic not in units:
            die("topic %r does not exist in config units - %s" % (topic, where))
        if typ not in TYPES:
            die("unknown type %r - %s" % (typ, where))
        if q2 in seen:
            die("duplicate question text - %s" % where)
        seen[q2] = idx
        if typ in ("mc", "fill"):
            if not isinstance(correct, int) or not 0 <= correct < len(opts) or len(opts) < 2:
                die("answer index out of range - %s" % where)
            if len(set(opts)) != len(opts):
                die("duplicate options - %s" % where)
        elif typ == "tf":
            if opts != ["True", "False"] or correct not in (0, 1):
                die("true/false must have options [True, False] and answer 0 or 1 - %s" % where)
        elif typ == "sata":
            if not correct or any(not 0 <= c < len(opts) for c in correct) or len(set(correct)) != len(correct):
                die("answer index out of range - %s" % where)
        elif typ == "order":
            if not 3 <= len(opts) <= 8 or list(correct) != list(range(len(opts))):
                die("order needs 3-8 steps keyed 0..n-1 - %s" % where)
        elif typ == "cloze":
            rows, ch = opts.get("rows", []), opts.get("choices", [])
            if not 3 <= len(rows) <= 4 or len(correct) != len(rows) or any(not 0 <= c < len(ch) for c in correct):
                die("matching table needs 3-4 rows with answers in range - %s" % where)
        elif typ == "blanks":
            if not 2 <= len(opts) <= 4 or len(correct) != len(opts) or any(not 0 <= c < len(o) for c, o in zip(correct, opts)):
                die("sentence needs 2-4 blanks with answers in range - %s" % where)
            if len(re.findall(r"\{\d\}", q2)) != len(opts):
                die("blank markers {1}.. do not match the blanks - %s" % where)
        items.append({"id": "q%d" % idx, "u": topic, "t": typ, "q": q2, "o": opts, "c": correct, "w": why,
                      "x": {}, "m": {}, "lp": False, "k": None, "src": "", "_q": q})

    byq = {it["_q"]: it for it in items}
    byq.update({it["q"]: it for it in items})

    def find(q, what):
        n = sum(1 for it in items if it["q"] == q or it["_q"] == q)
        if n != 1:
            die("%s matches %d questions (needs exactly 1): %r" % (what, n, q[:90]))
        return byq[q]

    # ---------------------------------------------------------------- rationales
    for q, w in gather(cfg, cfg_dir, "rationales", "WHY", "dict").items():
        find(q, "rationale")["w"] = w

    # ---------------------------------------------------------------- explanations / misconceptions
    def attach(table, field, what):
        for q, per in table.items():
            it = find(q, what)
            for opt, text in per.items():
                t, o, c = it["t"], it["o"], it["c"]
                if t in ("mc", "fill", "tf", "sata"):
                    if opt not in o:
                        die("%s for %r matches no option of %r" % (what, opt, q[:70]))
                    i = o.index(opt)
                    if (t == "sata" and i in c) or (t != "sata" and i == c):
                        die("%s attached to a CORRECT option %r of %r" % (what, opt, q[:70]))
                    it[field][str(i)] = text
                elif t == "cloze":
                    ch = o["choices"]
                    if opt not in ch:
                        die("%s for %r matches no choice of %r" % (what, opt, q[:70]))
                    i = ch.index(opt)
                    if i in c:
                        die("%s attached to a choice that is a correct answer (%r) of %r" % (what, opt, q[:70]))
                    it[field][str(i)] = text
                elif t == "blanks":
                    hits = [(b, oo.index(opt)) for b, oo in enumerate(o) if opt in oo and oo.index(opt) != c[b]]
                    if not hits:
                        if any(opt in oo for oo in o):
                            die("%s attached to a CORRECT option %r of %r" % (what, opt, q[:70]))
                        die("%s for %r matches no option of %r" % (what, opt, q[:70]))
                    for b, i in hits:
                        it[field]["%d:%d" % (b, i)] = text
                else:
                    die("%s given for a %s question %r" % (what, t, q[:70]))

    attach(gather(cfg, cfg_dir, "explanations", "EXPLAIN", "dict"), "x", "explanation")
    attach(gather(cfg, cfg_dir, "misconceptions", "MISC", "dict"), "m", "misconception")

    # ---------------------------------------------------------------- last pass
    for q in gather(cfg, cfg_dir, "last_pass", "LAST_PASS", "list"):
        find(q, "last-pass entry")["lp"] = True
    for tag in cfg.get("last_pass_tags") or []:
        for it in items:
            if tag in it["w"]:
                it["lp"] = True

    # ---------------------------------------------------------------- row stems
    for q, rows in gather(cfg, cfg_dir, "row_stems", "ROW_STEMS", "dict").items():
        it = find(q, "row stem")
        if it["t"] != "cloze":
            die("row stems given for a non-matching question %r" % q[:70])
        it["rs"] = {}
        for prompt, stem in rows.items():
            if prompt not in it["o"]["rows"]:
                die("row stem prompt %r is not a row of %r" % (prompt, q[:70]))
            it["rs"][str(it["o"]["rows"].index(prompt))] = stem

    # ---------------------------------------------------------------- numeric
    for q, spec in gather(cfg, cfg_dir, "numeric", "NUMERIC", "dict").items():
        it = find(q, "numeric entry")
        if it["t"] not in ("mc", "fill"):
            die("numeric entry must key an mc or fill question: %r" % q[:70])
        keyed = it["o"][it["c"]]
        try:
            val = float(re.sub(r"[^0-9.\-]", "", keyed))
        except ValueError:
            die("keyed option %r is not a number for %r" % (keyed, q[:70]))
        if abs(val - float(spec["answer"])) > 1e-9:
            die("numeric answer %r does not equal the keyed option %r for %r" % (spec["answer"], keyed, q[:70]))
        it["num"] = {"answer": spec["answer"], "unit": spec.get("unit", ""), "accept": spec.get("accept", {}), "near": spec.get("near", {})}

    # ---------------------------------------------------------------- concepts
    concepts, owner = {}, {}
    allc = gather(cfg, cfg_dir, "concepts", "CONCEPTS", "list")
    full = [c for c in allc if "title" in c]
    for c in [c for c in allc if "title" not in c]:   # {"id", "items"} adds questions to a card defined elsewhere
        tgt = [f for f in full if f["id"] == c["id"]]
        if not tgt:
            die("questions added to concept %r, which no content file defines" % c["id"])
        tgt[0]["items"] = tgt[0]["items"] + c["items"]
    for c in full:
        if c["unit"] not in units:
            die("concept %r has unknown topic %r" % (c["id"], c["unit"]))
        if c["id"] in concepts:
            die("duplicate concept id %r" % c["id"])
        ids = []
        for q in c["items"]:
            it = find(q, "concept %s item" % c["id"])
            if it["id"] in owner:
                die("question belongs to two concepts (%s, %s): %r" % (owner[it["id"]], c["id"], q[:70]))
            owner[it["id"]] = c["id"]
            it["k"] = c["id"]
            ids.append(it["id"])
        concepts[c["id"]] = {"title": c["title"], "unit": c["unit"], "points": c["points"], "source": c["source"], "items": ids}

    # ---------------------------------------------------------------- guide link check
    g = cfg.get("guide")
    if g:
        idx_path = os.path.normpath(os.path.join(cfg_dir, g["index_out"]))
        if not os.path.exists(idx_path):
            die("guide index %s not found - run build-guide.py first (build-exam.py does both)" % idx_path)
        gindex = json.load(open(idx_path))
        links = getattr(load(cfg_dir, g["links"]), "LINKS")
        for cid, c in concepts.items():
            if cid not in links:
                die("concept %r has no guide link in %s" % (cid, g["links"]))
            secs = links[cid].split()
            for s in secs:
                if s not in gindex:
                    die("concept %r links to guide section %r, which does not exist" % (cid, s))
            text = " ".join(gindex[s]["text"] for s in secs)
            for pnt in c["points"]:
                if norm(pnt) not in text:
                    die("card fact not found in its linked guide section(s) %s:\n  concept %s: %r" % (secs, cid, pnt))
            c["sec"] = [{"id": s, "title": gindex[s]["title"], "key": gindex[s]["key"]} for s in secs]
        for cid in links:
            if cid not in concepts:
                die("guide link for unknown concept %r" % cid)

    # ---------------------------------------------------------------- finishing fields
    for it in items:
        m = re.search(r"\(([^()]*)\)\s*$", it["w"])
        it["src"] = m.group(1) if m else "materials"
        it["kind"] = kind_of(it["q"], it["t"], "num" in it)
        del it["_q"]

    # ---------------------------------------------------------------- counts
    def n_wrong(it):
        t, o, c = it["t"], it["o"], it["c"]
        if t in ("mc", "fill"):
            return len(o) - 1
        if t == "tf":
            return 1
        if t == "sata":
            return len(o) - len(c)
        if t == "blanks":
            return sum(len(x) - 1 for x in o)
        if t == "cloze":
            return len([i for i in range(len(o["choices"])) if i not in c])
        return 0
    total_wrong = sum(n_wrong(it) for it in items)
    explained = sum(len(it["x"]) for it in items if "num" not in it) + sum(len(it["x"]) for it in items if "num" in it)
    covered = sum(1 for it in items if it["k"])
    lp = sum(1 for it in items if it["lp"])
    tf_bad = []
    print("questions: %d" % len(items))
    for u in units:
        us = [it for it in items if it["u"] == u]
        tfs = [it for it in us if it["t"] == "tf"]
        ntrue = sum(1 for it in tfs if it["c"] == 0)
        if tfs and ntrue * 2 != len(tfs):
            tf_bad.append(u)
        fm = {}
        for it in us:
            k = "numeric" if "num" in it else it["t"]
            fm[k] = fm.get(k, 0) + 1
        print("  %-13s %3d  %s  | true/false %d true of %d" % (u, len(us), " ".join("%s %d" % kv for kv in sorted(fm.items())), ntrue, len(tfs)))
    if tf_bad:
        die("true/false is not half true and half false in: %s" % ", ".join(tf_bad))
    fmt = {}
    for it in items:
        k = "numeric" if "num" in it else it["t"]
        fmt[k] = fmt.get(k, 0) + 1
    print("formats: " + ", ".join("%s %d" % kv for kv in sorted(fmt.items())))
    print("duplicates: 0 (refused otherwise)")
    print("explained %d of %d wrong options" % (explained, total_wrong))
    print("concepts: %d, questions covered %d of %d" % (len(concepts), covered, len(items)))
    print("misconception labels: %d" % sum(len(it["m"]) for it in items))
    print("row stems: %d matching tables" % sum(1 for it in items if it.get("rs")))
    print("numeric (typed): %d" % sum(1 for it in items if "num" in it))
    print("last pass %d questions" % lp)
    if explained < total_wrong:
        missing = [(it["q"][:60], n_wrong(it) - len(it["x"])) for it in items if n_wrong(it) > len(it["x"])]
        die("%d wrong options have no explanation, e.g. %r" % (total_wrong - explained, missing[:3]))
    if covered < len(items):
        die("%d questions are on no concept card" % (len(items) - covered))

    data = {
        "cfg": {"title": cfg["title"], "eyebrow": cfg.get("eyebrow", ""), "storage_key": cfg["storage_key"],
                "units": units, "high_roi_units": cfg.get("high_roi_units") or [],
                "last_pass_note": cfg.get("last_pass_note", ""),
                "guide_url": (g or {}).get("url", ""), "hub_url": cfg.get("hub_url", ""), "pretest_per_topic": cfg.get("pretest_per_topic"), "guide_title": (g or {}).get("title", "")},
        "items": items, "concepts": concepts,
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    tpl = open(os.path.join(ENGINE, "drill-template.html")).read()
    core = open(os.path.join(ENGINE, "drill-core.js")).read()
    readme = open(os.path.join(ENGINE, "readme-study-system.html")).read()
    page = (tpl.replace("/*__CORE__*/", core)
               .replace("/*__DATA__*/", "var DATA = " + blob + ";")
               .replace("<!--__README__-->", readme)
               .replace("__TITLE__", html.escape(cfg["title"]))
               .replace("__EYEBROW__", html.escape(cfg.get("eyebrow", ""))))
    out_path = os.path.normpath(os.path.join(cfg_dir, cfg["out"]))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w").write(page)
    json.dump(data, open(out_path.replace(".html", ".data.json"), "w"), ensure_ascii=False)
    print("drill -> %s (%d KB)" % (out_path, len(page.encode()) // 1024))
    return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
