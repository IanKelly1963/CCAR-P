"""Per-question checks for a gap staging file: gap/new_<tag>.json
Shape: {"gaps":[{"subject","area","source","summary","question_count"}], "questions":[{subject, concept, type, stem, options, correct, explanation, mnemonic}]}
"""
import json, re, sys, os

def wc(s):
    return len(re.findall(r"\S+", s))

here = os.path.dirname(os.path.abspath(__file__))
subjects = set()
for n in range(1, 8):
    d = json.load(open(os.path.join(here, "..", "data", f"d{n}.json"), encoding="utf8"))
    subjects.update(s["id"] for s in d["subjects"])

d = json.load(open(sys.argv[1], encoding="utf8"))
probs = []
longest = 0
for k, q in enumerate(d["questions"]):
    tag = f"q[{k}] {q.get('subject')} {q.get('concept')}"
    if q.get("subject") not in subjects:
        probs.append(f"{tag}: unknown subject id")
    for f in ("concept", "type", "stem", "options", "correct", "explanation", "mnemonic"):
        if f not in q or q[f] in ("", []):
            probs.append(f"{tag}: missing {f}")
    n = len(q["options"])
    if q["type"] == "single":
        if n != 4 or len(q["correct"]) != 1:
            probs.append(f"{tag}: single needs 4 options / 1 correct")
    elif q["type"] == "multi":
        if n not in (4, 5) or len(q["correct"]) not in (2, 3):
            probs.append(f"{tag}: multi needs 4-5 options / 2-3 correct")
        w = {2: "TWO", 3: "THREE"}.get(len(q["correct"]))
        if w and w not in q["stem"]:
            probs.append(f"{tag}: multi stem must say 'Select {w}'")
    else:
        probs.append(f"{tag}: bad type")
    if any(c < 0 or c >= n for c in q["correct"]) or len(set(q["correct"])) != len(q["correct"]):
        probs.append(f"{tag}: bad correct indexes")
    if wc(q["mnemonic"]) > 22:
        probs.append(f"{tag}: mnemonic too long")
    for o in q["options"]:
        if re.match(r"^\s*[A-E][\.\)]\s", o) or re.search(r"all of the above|none of the above", o, re.I):
            probs.append(f"{tag}: bad option text")
    cl = [wc(q["options"][i]) for i in q["correct"]]
    dl = [wc(o) for i, o in enumerate(q["options"]) if i not in q["correct"]]
    ca, da = sum(cl) / len(cl), sum(dl) / len(dl)
    if ca / da > 1.3 or ca / da < 0.75:
        probs.append(f"{tag}: length parity off ({ca:.1f} vs {da:.1f} words)")
    if max(cl) > max(dl):
        longest += 1
nq = len(d["questions"])
pct = 100 * longest / max(1, nq)
print(f"{nq} questions, {len(d['gaps'])} gap areas, correct-is-longest {pct:.0f}%")
if nq and pct > 55:
    probs.append("correct answer is the longest option too often")
if probs:
    print("PROBLEMS:"); [print(" -", p) for p in probs]; sys.exit(1)
print("OK")
