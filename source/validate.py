import json, sys, re, collections

def wc(s):
    return len(re.findall(r"\S+", s))

def main(path):
    d = json.load(open(path, encoding="utf8"))
    problems = []
    total = 0
    pos = collections.Counter()
    longest_correct = 0
    nq = 0
    for s in d["subjects"]:
        qs = s["questions"]
        total += len(qs)
        if len(qs) < 11:
            problems.append(f"{s['id']}: only {len(qs)} questions (<11)")
        if not (4 <= len(s["learn"]) <= 6):
            problems.append(f"{s['id']}: learn bullets {len(s['learn'])} (want 4-6)")
        if not (3 <= len(s["traps"]) <= 5):
            problems.append(f"{s['id']}: trap bullets {len(s['traps'])} (want 3-5)")
        concepts = collections.Counter(q["concept"] for q in qs)
        pairs = sum(1 for c, n in concepts.items() if n >= 2)
        if pairs < 4:
            problems.append(f"{s['id']}: only {pairs} concepts asked twice (want >=4)")
        multi = sum(1 for q in qs if q["type"] == "multi")
        if multi < max(2, len(qs) // 6):
            problems.append(f"{s['id']}: only {multi} multi questions")
        ids = set()
        for q in qs:
            nq += 1
            qid = q["id"]
            if qid in ids:
                problems.append(f"{qid}: duplicate id")
            ids.add(qid)
            n = len(q["options"])
            if q["type"] == "single":
                if n != 4 or len(q["correct"]) != 1:
                    problems.append(f"{qid}: single needs 4 options/1 correct (has {n}/{len(q['correct'])})")
            else:
                if n not in (4, 5) or len(q["correct"]) not in (2, 3):
                    problems.append(f"{qid}: multi needs 4-5 options and 2-3 correct")
                words = {2: "TWO", 3: "THREE"}.get(len(q["correct"]), "?")
                if words not in q["stem"]:
                    problems.append(f"{qid}: multi stem must say 'Select {words}'")
            if any(c < 0 or c >= n for c in q["correct"]) or len(set(q["correct"])) != len(q["correct"]):
                problems.append(f"{qid}: bad correct indexes")
            for k in ("explanation", "mnemonic", "stem", "concept"):
                if not q.get(k, "").strip():
                    problems.append(f"{qid}: missing {k}")
            if wc(q["mnemonic"]) > 22:
                problems.append(f"{qid}: mnemonic too long ({wc(q['mnemonic'])} words)")
            if len(set(o.strip().lower() for o in q["options"])) != n:
                problems.append(f"{qid}: duplicate options")
            for o in q["options"]:
                if re.match(r"^\s*[A-E][\.\)]\s", o):
                    problems.append(f"{qid}: option has letter prefix")
                if re.search(r"all of the above|none of the above", o, re.I):
                    problems.append(f"{qid}: forbidden option phrase")
            cl = [wc(q["options"][i]) for i in q["correct"]]
            dl = [wc(o) for i, o in enumerate(q["options"]) if i not in q["correct"]]
            ca, da = sum(cl) / len(cl), sum(dl) / len(dl)
            if da and (ca / da > 1.3 or ca / da < 0.75):
                problems.append(f"{qid}: length parity off (correct avg {ca:.1f}w vs distractor avg {da:.1f}w)")
            if max(cl) > max(dl):
                longest_correct += 1
            if q["type"] == "single":
                pos[q["correct"][0]] += 1
    print(f"questions={total} subjects={len(d['subjects'])} positions(single)={dict(pos)}")
    pct = 100 * longest_correct / max(1, nq)
    print(f"correct-is-longest in {pct:.0f}% of questions (ideal ~25-45%)")
    if pct > 55:
        problems.append(f"correct answer is the longest option too often ({pct:.0f}%)")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("OK")

main(sys.argv[1])
