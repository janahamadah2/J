# Exam drill engine

One config + content files -> a Mastery Study Guide page and an active-recall Drill page.

    python3 engine/build-exam.py exams/cvs-mid2/config-cvs-mid2.json   # guide, then drill (validates everything)
    node engine/simulate.js dist/cvs-mid2-drill.data.json               # answer letters, T/F, session repeats, pre-test, timed plans

- `engine/drill-template.html` + `engine/drill-core.js`: all drill behaviour (the core is also what simulate.js runs).
- `engine/build-drill.py`, `engine/build-guide.py` + `engine/guide-shell.html`, shared `engine/readme-study-system.html`.
- `exams/cvs-mid2/`: `items-cvs-mid2-<topic>.py` (ITEMS, EXPLAIN, MISC, LAST_PASS, CONCEPTS, ROW_STEMS, NUMERIC per topic),
  `guide-cvs-mid2-<topic>.py` (guide sections), `guide-links-cvs-mid2.py`, `config-cvs-mid2.json`.
- New exam: copy the config, write new content files, add new item files at the END of `items_module` (ids follow file order).

Published: drill https://claude.ai/artifact/F16ffDggDNEKMrvNsnAP4D · guide https://claude.ai/artifact/A1TLoMo73wpzbXEL8EnYGF
