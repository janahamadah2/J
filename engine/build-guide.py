#!/usr/bin/env python3
"""Build the Mastery Study Guide page from a drill config.

    python3 engine/build-guide.py exams/cvs-mid2/config-cvs-mid2.json

Reads config["guide"]["parts"] (each a .py file with SECTIONS), renders
engine/guide-shell.html with the shared Read me, and writes the guide page and
a section index (JSON) that build-drill.py uses to show each concept's Key ideas
and to check that every concept-card fact appears in its linked section.
"""
import html
import importlib.util
import json
import os
import re
import sys

ENGINE = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ["id", "unit", "title", "key", "mechanism", "actions", "example", "trap", "trick", "blanks"]


def die(msg):
    sys.exit("build-guide: REFUSED - " + msg)


def load_module(path, name):
    sys.path.insert(0, os.path.dirname(path))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sys.path.pop(0)
    return mod


def norm(text):
    """Plain, comparable text: no tags, no [[ ]], straight quotes, one space, lower case."""
    t = re.sub(r"<[^>]+>", " ", text)
    t = html.unescape(t).replace("[[", "").replace("]]", "")
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t).strip().lower()


def blank_html(s):
    out, i = [], 0
    for m in re.finditer(r"\[\[(.+?)\]\]", s):
        out.append(s[i:m.start()])
        ans = m.group(1)
        out.append('<button type="button" class="blank" aria-label="Tap to reveal">'
                   '<span class="ans">%s</span></button>' % ans)
        i = m.end()
    out.append(s[i:])
    return "".join(out)


def esc(s):
    """Content is trusted author HTML (only <b>/<i>); escape bare ampersands."""
    return re.sub(r"&(?![a-zA-Z#0-9]+;)", "&amp;", s)


def section_html(s, num):
    li = lambda xs: "".join("<li>%s</li>" % esc(x) for x in xs)
    return f"""
<section class="sec" id="{s['id']}" data-unit="{html.escape(s['unit'])}">
  <p class="sec-eyebrow">{html.escape(s['unit'])} · {num}</p>
  <h3>{html.escape(s['title'])}</h3>
  <div class="block mech"><h4>How it works</h4><p>{esc(s['mechanism'])}</p></div>
  <div class="block"><h4>What to do first</h4><ol>{li(s['actions'])}</ol></div>
  <div class="block"><h4>Client example</h4><p>{esc(s['example'])}</p></div>
  <div class="block trap"><h4>Common trap</h4><p>{esc(s['trap'])}</p></div>
  <div class="block"><h4>Memory trick</h4><p>{esc(s['trick'])}</p></div>
  <div class="block"><h4>Test yourself <span class="hint">tap each blank</span></h4><ul class="blanks">{''.join('<li>%s</li>' % blank_html(esc(b)) for b in s['blanks'])}</ul></div>
  <div class="key"><h4>Key ideas</h4><ul>{li(s['key'])}</ul></div>
  <p class="src">Source: {html.escape(s.get('source', ''))}</p>
</section>"""


def build(cfg_path):
    cfg_dir = os.path.dirname(os.path.abspath(cfg_path))
    cfg = json.load(open(cfg_path))
    g = cfg.get("guide")
    if not g:
        die("config has no 'guide' block")
    sections, seen = [], set()
    for i, part in enumerate(g["parts"]):
        mod = load_module(os.path.join(cfg_dir, part), "guide_part_%d" % i)
        for s in getattr(mod, "SECTIONS", []):
            for f in REQUIRED:
                if f not in s or s[f] in ("", [], None):
                    die("section %r in %s is missing %r" % (s.get("id"), part, f))
            if s["id"] in seen:
                die("duplicate section id %r" % s["id"])
            if s["unit"] not in cfg["units"]:
                die("section %r has unknown topic %r" % (s["id"], s["unit"]))
            seen.add(s["id"])
            sections.append(s)
    # lecture order = topic order, then file order
    sections.sort(key=lambda s: cfg["units"].index(s["unit"]))
    readme = open(os.path.join(ENGINE, "readme-study-system.html")).read()
    toc, body, counter = [], [], {}
    for s in sections:
        counter[s["unit"]] = counter.get(s["unit"], 0) + 1
        num = counter[s["unit"]]
        if num == 1:
            toc.append('<li class="toc-unit">%s</li>' % html.escape(s["unit"]))
            body.append('<h2 class="unit-h" id="unit-%s">%s</h2>' % (re.sub(r"\W+", "-", s["unit"].lower()), html.escape(s["unit"])))
        toc.append('<li><a href="#%s">%s</a></li>' % (s["id"], html.escape(s["title"])))
        body.append(section_html(s, num))
    shell = open(os.path.join(ENGINE, "guide-shell.html")).read()
    out = (shell.replace("__TITLE__", html.escape(g["title"]))
                .replace("__EYEBROW__", html.escape(cfg.get("eyebrow", "")))
                .replace("__DRILL_URL__", html.escape(g.get("drill_url") or ""))
                .replace("__HUB_URL__", html.escape(cfg.get("hub_url") or ""))
                .replace("<!--__README__-->", readme)
                .replace("<!--__TOC__-->", "\n".join(toc))
                .replace("<!--__SECTIONS__-->", "\n".join(body))
                .replace("__NSEC__", str(len(sections))))
    out_path = os.path.normpath(os.path.join(cfg_dir, g["out"]))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w").write(out)
    index = {}
    for s in sections:
        full = " ".join([s["title"], s["mechanism"], s["example"], s["trap"], s["trick"]] +
                        s["actions"] + s["blanks"] + s["key"])
        index[s["id"]] = {"title": s["title"], "unit": s["unit"], "key": s["key"], "text": norm(full)}
    idx_path = os.path.normpath(os.path.join(cfg_dir, g["index_out"]))
    json.dump(index, open(idx_path, "w"), ensure_ascii=False, indent=0)
    print("guide: %d sections, %d topics -> %s (%d KB)" % (len(sections), len(counter), out_path, len(out) // 1024))
    return index


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
