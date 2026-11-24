"""Authoring helpers for content files.

Each topic file creates one Bank, writes questions with it, then exports the
standard content names the engine reads (ITEMS, EXPLAIN, MISC, LAST_PASS,
CONCEPTS, ROW_STEMS, NUMERIC).  Options are written correct-first; the drill
shuffles them on screen with balanced answer letters.

A wrong option is written as (text, "why it is wrong") or
(text, "why it is wrong", "short misconception label").
"""


class Bank:
    def __init__(self, topic):
        self.topic = topic
        self.items, self.explain, self.misc = [], {}, {}
        self.last, self.concepts, self.row_stems, self.numeric = [], [], {}, {}
        self.cur = None

    # concept cards: every question written after concept() joins it
    def concept(self, cid, title, points, source):
        self.cur = {"id": cid, "unit": self.topic, "title": title,
                    "points": points, "source": source, "items": []}
        self.concepts.append(self.cur)

    def _add(self, typ, q, options, correct, why, src, last):
        q = " ".join(q.split())
        self.items.append((self.topic, typ, q, options, correct,
                           " ".join(why.split()) + " (" + src + ")"))
        if self.cur is not None:
            self.cur["items"].append(q)
        if last:
            self.last.append(q)
        return q

    def _wrongs(self, q, wrongs, key=lambda w: w[0]):
        ex, mi = {}, {}
        for w in wrongs:
            ex[key(w)] = w[1]
            if len(w) > 2 and w[2]:
                mi[key(w)] = w[2]
        if ex:
            self.explain.setdefault(q, {}).update(ex)
        if mi:
            self.misc.setdefault(q, {}).update(mi)

    def mc(self, q, right, wrongs, why, src, last=False, typ="mc", numeric=None):
        q = self._add(typ, q, [right] + [w[0] for w in wrongs], 0, why, src, last)
        self._wrongs(q, wrongs)
        if numeric:
            self.numeric[q] = numeric
        return q

    def fill(self, q, right, wrongs, why, src, last=False):
        return self.mc(q, right, wrongs, why, src, last, typ="fill")

    def sata(self, q, rights, wrongs, why, src, last=False):
        q = " ".join(q.split())
        if "Select all that apply." not in q:
            q += " Select all that apply."
        q = self._add("sata", q, rights + [w[0] for w in wrongs],
                      list(range(len(rights))), why, src, last)
        self._wrongs(q, wrongs)
        return q

    def tf(self, q, truth, why, src, wrong_why, label=None, last=False):
        q = self._add("tf", q, ["True", "False"], 0 if truth else 1, why, src, last)
        w = ("False" if truth else "True", wrong_why, label)
        self._wrongs(q, [w])
        return q

    def order(self, q, steps, why, src, last=False):
        return self._add("order", q, list(steps), list(range(len(steps))), why, src, last)

    def match(self, q, rows, extra, why, src, row_stems=None, last=False):
        """rows: [(prompt, answer)]; extra: [(distractor, why[, label])]."""
        choices = []
        for _, a in rows:
            if a not in choices:
                choices.append(a)
        choices += [e[0] for e in extra]
        correct = [choices.index(a) for _, a in rows]
        q = self._add("cloze", q, {"rows": [r for r, _ in rows], "choices": choices},
                      correct, why, src, last)
        self._wrongs(q, extra)
        if row_stems:
            self.row_stems[q] = row_stems
        return q

    def blanks(self, q, slots, why, src, last=False):
        """q holds {1} {2} ... ; slots: [(right, [(wrong, why[, label])...])]."""
        opts = [[r] + [w[0] for w in ws] for r, ws in slots]
        q = self._add("blanks", q, opts, [0] * len(slots), why, src, last)
        for _, ws in slots:
            self._wrongs(q, ws)
        return q

    def export(self):
        return (self.items, self.explain, self.misc, self.last, self.concepts,
                self.row_stems, self.numeric)
