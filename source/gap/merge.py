"""Merge gap staging files (gap/new_*.json) into data/dN.json and write gap/GAP_REPORT.md.
Usage:  python gap/merge.py            -> dry run: prints plan + cross-file concept overlaps
        python gap/merge.py --apply    -> appends questions to the banks (ids continue each subject's numbering)
Questions listed in gap/skip.txt (lines "<tag> <index>") are left out.
"""
import json, glob, os, re, sys, collections

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
apply = "--apply" in sys.argv

banks = {n: json.load(open(os.path.join(root, "data", f"d{n}.json"), encoding="utf8")) for n in range(1, 8)}
subj = {s["id"]: s for b in banks.values() for s in b["subjects"]}

skip = set()
sp = os.path.join(here, "skip.txt")
if os.path.exists(sp):
    for line in open(sp, encoding="utf8"):
        p = line.split("#")[0].split()
        if len(p) == 2:
            skip.add((p[0], int(p[1])))

staged, gaps = [], []
for f in sorted(glob.glob(os.path.join(here, "new_*.json"))):
    tag = os.path.basename(f)[4:-5]
    d = json.load(open(f, encoding="utf8"))
    for g in d["gaps"]:
        gaps.append({**g, "tag": tag})
    for k, q in enumerate(d["questions"]):
        if (tag, k) not in skip:
            staged.append((tag, k, q))

# overlap report: same concept, or same subject + heavily shared stem words, across different files
def words(s):
    return set(w for w in re.findall(r"[a-z]{5,}", s.lower()))
print(f"{len(staged)} staged questions from {len({t for t,_,_ in staged})} files; {len(gaps)} gap areas; {len(skip)} skipped")
seen = collections.defaultdict(list)
for tag, k, q in staged:
    seen[q["concept"]].append((tag, k))
for c, v in seen.items():
    if len({t for t, _ in v}) > 1:
        print("CONCEPT OVERLAP", c, v)
for i, (t1, k1, q1) in enumerate(staged):
    for t2, k2, q2 in staged[i + 1:]:
        if t1 != t2 and q1["subject"] == q2["subject"]:
            a, b = words(q1["stem"] + " " + " ".join(q1["options"][j] for j in q1["correct"])), words(q2["stem"] + " " + " ".join(q2["options"][j] for j in q2["correct"]))
            if a and b and len(a & b) / min(len(a), len(b)) > 0.5:
                print(f"POSSIBLE DUP {t1} {k1} ~ {t2} {k2}: {q1['stem'][:70]!r}")

if not apply:
    sys.exit(0)

added = collections.defaultdict(list)
for tag, k, q in staged:
    s = subj[q["subject"]]
    nums = [int(re.search(r"q(\d+)$", x["id"]).group(1)) for x in s["questions"]]
    q = {k2: v for k2, v in q.items() if k2 != "subject"}
    q["id"] = f"{s['id']}q{max(nums) + 1:02d}"
    s["questions"].append(dict(id=q["id"], concept=q["concept"], type=q["type"], stem=q["stem"], options=q["options"],
                               correct=q["correct"], explanation=q["explanation"], mnemonic=q["mnemonic"]))
    added[s["id"]].append(q)
for n, b in banks.items():
    json.dump(b, open(os.path.join(root, "data", f"d{n}.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)

# report
rep = ["# Gap report: content in the notes not previously tested", ""]
for n in range(1, 8):
    rows = [g for g in gaps if g["subject"].startswith(f"d{n}s")]
    if not rows:
        continue
    rep.append(f"## Domain {n}")
    rep.append("| Subject | Missing area | Source | New questions |")
    rep.append("|---|---|---|---|")
    for g in sorted(rows, key=lambda g: g["subject"]):
        rep.append(f"| {g['subject']} {subj[g['subject']]['title']} | {g['area']} | {g['source']} | {g.get('question_count','')} |")
    rep.append("")
rep.append("## Questions added per subject")
for sid in sorted(added):
    rep.append(f"- {sid} {subj[sid]['title']}: +{len(added[sid])} ({', '.join(q['id'] for q in added[sid])})")
open(os.path.join(here, "GAP_REPORT.md"), "w", encoding="utf8").write("\n".join(rep))
print(f"applied {sum(len(v) for v in added.values())} questions to {len(added)} subjects; wrote gap/GAP_REPORT.md")
