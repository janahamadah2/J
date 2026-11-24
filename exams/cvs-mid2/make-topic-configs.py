#!/usr/bin/env python3
"""Make one stand-alone drill + guide config per topic from the master config.

    python3 exams/cvs-mid2/make-topic-configs.py      # writes topics/config-cvs-mid2-<topic>.json
    for f in exams/cvs-mid2/topics/config-*.json; do python3 engine/build-exam.py "$f"; done

Each topic gets its own storage key (its own saved progress), its own guide-links
file and its own output pages. URLs live in topics/urls.json and are filled in
after the first publish.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
master = json.load(open(os.path.join(HERE, "config-cvs-mid2.json")))
out_dir = os.path.join(HERE, "topics")
os.makedirs(out_dir, exist_ok=True)
urls_path = os.path.join(out_dir, "urls.json")
urls = json.load(open(urls_path)) if os.path.exists(urls_path) else {}

ns = {}
exec(open(os.path.join(HERE, "guide-links-cvs-mid2.py")).read(), ns)
LINKS = ns["LINKS"]

for topic in master["units"]:
    slug = topic.lower()
    item_file = "../items-cvs-mid2-%s.py" % slug
    extra = ["../" + os.path.basename(x) for x in master["items_module"]
             if os.path.basename(x).startswith("items-cvs-mid2-%s-" % slug)]   # uploaded banks, added after the topic's own file
    files = [item_file] + extra
    guide_file = "../guide-cvs-mid2-%s.py" % slug
    # links for this topic's concepts only (concept ids come from the guide part's section ids)
    gns = {}
    exec(open(os.path.join(HERE, "guide-cvs-mid2-%s.py" % slug)).read(), gns)
    ids = [s["id"] for s in gns["SECTIONS"]]
    links_name = "guide-links-cvs-mid2-%s.py" % slug
    with open(os.path.join(out_dir, links_name), "w") as f:
        f.write('"""Concept card -> guide section links for %s (generated from ../guide-links-cvs-mid2.py)."""\n' % topic)
        f.write("LINKS = {\n" + "".join('    "%s": "%s",\n' % (i, LINKS[i]) for i in ids) + "}\n")
    u = urls.get(slug, {})
    numeric = [item_file] if any(item_file.endswith(os.path.basename(p)) for p in master.get("numeric", [])) else []
    cfg = {
        "title": "CVS Mid 2 %s Drill" % topic,
        "eyebrow": "CVS block · Mid 2 · %s only · Sunday 29 November 2026" % topic,
        "storage_key": "cvs-mid2-2026-11-29-%s" % slug,
        "units": [topic],
        "out": "../../../dist/topics/cvs-mid2-%s-drill.html" % slug,
        "deck": None,
        "items_module": files,
        "explanations": files, "misconceptions": files, "concepts": files,
        "row_stems": files, "numeric": numeric, "last_pass": files,
        "rationales": [], "item_overrides": [], "deck_overrides": [],
        "high_roi_units": [],
        "pretest_per_topic": 10,
        "last_pass_tags": master["last_pass_tags"],
        "last_pass_note": ("The %s questions from the Shams Practices bank, the cases asked in class, slide exercises and facts flagged on slides with NOTE, N.B. or REMEMBER." if extra else "The %s questions taken from cases asked in class, slide exercises and facts flagged on slides with NOTE, N.B. or REMEMBER.") % topic,
        "hub_url": urls.get("hub", ""),
        "guide": {
            "parts": [guide_file],
            "title": "CVS Mid 2 %s Guide" % topic,
            "out": "../../../dist/topics/cvs-mid2-%s-guide.html" % slug,
            "index_out": "../../../dist/topics/cvs-mid2-%s-guide-index.json" % slug,
            "url": u.get("guide", ""),
            "drill_url": u.get("drill", ""),
            "links": links_name,
        },
    }
    json.dump(cfg, open(os.path.join(out_dir, "config-cvs-mid2-%s.json" % slug), "w"), indent=2, ensure_ascii=False)
    print("wrote", "config-cvs-mid2-%s.json" % slug)
