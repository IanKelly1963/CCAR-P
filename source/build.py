import json, glob, os
sp = os.path.dirname(os.path.abspath(__file__))
doms = []
for n in range(1, 8):
    p = os.path.join(sp, "data", f"d{n}.json")
    doms.append(json.load(open(p, encoding="utf8")))
tpl = open(os.path.join(sp, "template.html"), encoding="utf8").read()
blob = json.dumps({"domains": doms}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
out = tpl.replace("/*__DATA__*/null", blob)
dest = os.path.join(os.path.dirname(sp), "CCAR-P Study Aid.html")
open(dest, "w", encoding="utf8").write(out)
nq = sum(len(s["questions"]) for d in doms for s in d["subjects"])
ns = sum(len(d["subjects"]) for d in doms)
print(f"built {dest}: {ns} subjects, {nq} questions, {len(out)//1024} KB")
