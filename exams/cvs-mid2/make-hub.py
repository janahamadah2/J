#!/usr/bin/env python3
"""Write dist/cvs-mid2-hub.html: one card per topic (drill + guide) plus the combined pages."""
import html, importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
urls = json.load(open(os.path.join(HERE, "topics", "urls.json")))
master = json.load(open(os.path.join(HERE, "config-cvs-mid2.json")))
LECT = {"Anatomy": "L4 blood supply and surface anatomy of the heart · L5 blood supply of the head and neck",
        "Physiology": "L6-L7 ECG · L8 cardiac output and venous return · L9 coronary circulation",
        "Pathology": "L1-L2 hemodynamic disorders · L3 rheumatic fever · L4 atherosclerosis",
        "Pharmacology": "L2-L4 treatment of hypertension",
        "Biochemistry": "L5 diet fat and CHD · L6 oxidative stress and atherosclerosis",
        "Microbiology": "L3 infective endocarditis",
        "Embryology": "L3 development of the aortic arches"}
cards = []
for t in master["units"]:
    slug = t.lower()
    sys.path.insert(0, HERE)
    nq = nb = nc = 0
    for f in master["items_module"]:
        if f == "items-cvs-mid2-%s.py" % slug or f.startswith("items-cvs-mid2-%s-" % slug):
            spec = importlib.util.spec_from_file_location(f, os.path.join(HERE, f))
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            nq += len(m.ITEMS); nc += len([c for c in m.CONCEPTS if "title" in c])
            if f != "items-cvs-mid2-%s.py" % slug: nb += len(m.ITEMS)
    u = urls[slug]
    cards.append(f"""<article class="t"><h2>{html.escape(t)}</h2><p class="m">{html.escape(LECT[t])}</p>
<p class="n">{nq} questions ({nb} from the Shams past papers) · {nc} guide sections</p>
<div class="b"><a class="btn p" href="{u['drill']}" target="_blank" rel="noopener">Drill</a><a class="btn" href="{u['guide']}" target="_blank" rel="noopener">Mastery guide</a></div></article>""")
a = urls["all"]
page = f"""<title>CVS Mid 2 Study Hub</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,700&family=Inter:wght@400;600&display=swap">
<style>
/* Layout: one column of topic cards in lecture order; combined pages last. */
:root {{ --bg:#fff; --fg:#111; --muted:#565c62; --line:#e2e4e7; --serif:"Source Serif 4",Georgia,serif; --sans:Inter,-apple-system,"Segoe UI",Roboto,Arial,sans-serif; color-scheme: light; }}
* {{ box-sizing:border-box; }}
body {{ background:var(--bg); color:var(--fg); font:16px/1.55 var(--sans); margin:0; }}
main {{ max-width:720px; margin:0 auto; padding-block:24px 60px; padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px)); }}
h1 {{ font:700 30px/1.2 var(--serif); margin:4px 0 6px; }}
h2 {{ font:700 21px/1.25 var(--serif); margin:0; }}
.e {{ font-size:13px; color:var(--muted); margin:0; }}
.t {{ border:1px solid var(--line); border-radius:12px; padding:14px 16px; margin:12px 0; }}
.t.all {{ border:1.5px solid var(--fg); }}
.m {{ color:var(--muted); font-size:14px; margin:4px 0; }}
.n {{ font-size:14px; margin:4px 0 10px; font-variant-numeric:tabular-nums; }}
.b {{ display:flex; flex-wrap:wrap; gap:8px; }}
.btn {{ border:1.5px solid var(--fg); border-radius:10px; padding:9px 16px; font-weight:600; color:var(--fg); text-decoration:none; min-height:44px; display:inline-flex; align-items:center; touch-action:manipulation; }}
.btn.p {{ background:var(--fg); color:var(--bg); }}
@media (hover:hover) {{ .btn:hover {{ background:#f4f5f6; }} .btn.p:hover {{ background:#333; }} }}
.btn:active {{ background:#e9ebee; }}
</style>
<main>
<p class="e">{html.escape(master['eyebrow'])}</p>
<h1>CVS Mid 2 Study Hub</h1>
<p>Each topic has its own drill (practice questions, pre-test, last pass, Fix my misses) and its own Mastery guide, in lecture order. Each topic drill keeps its own progress.</p>
{''.join(cards)}
<article class="t all"><h2>All topics together</h2><p class="m">Mixed practice across all seven topics, for the final days before the exam. Progress here is kept separately from the topic drills.</p>
<div class="b"><a class="btn p" href="{a['drill']}" target="_blank" rel="noopener">Combined drill</a><a class="btn" href="{a['guide']}" target="_blank" rel="noopener">Combined guide</a></div></article>
</main>
"""
out = os.path.normpath(os.path.join(HERE, "../../dist/cvs-mid2-hub.html"))
open(out, "w").write(page)
print("hub ->", out)
