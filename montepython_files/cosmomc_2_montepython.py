import re

import sys

prmf = open(sys.argv[2])
extr = [open(v) for v in sys.argv[3:]]
res = open(sys.argv[1],"w")

prms = {}
priors = {}
latex = {}

for e in extr:
  for l in e:
    l = l.split("#")[0]
    #print(l)
    if not l.strip():
      continue
    if l.startswith("param["):
      prs = l[len("param["):].split("]")[0]
      vls = [float(v) for v in l.split("=")[1].strip().split()]
      prms[prs] = vls
      continue
    if l.startswith("prior["):
      prs = l[len("prior["):].split("]")[0]
      vls = [float(v) for v in l.split("=")[1].strip().split()]
      priors[prs] = vls
      continue

for l in prmf:
  l = l.split("#")[0]
  if not l.strip():
    continue
  latex[l.split()[0]]=" ".join(l.split()[1:])

for p in prms:
  print(" PRMS ",p)
  print(p,":",file=res)
  if p in latex:
    print("  latex: ",latex[p],file=res)
  if len(prms[p])==1:
    print("  value: ",prms[p][0],file=res)
  else:
    print("  prior:\n    min: %g\n    max: %g"%(prms[p][1],prms[p][2]),file=res)
    print("  ref:\n    dist: norm\n    loc: %g\n    scale: %g"%(prms[p][0],prms[p][3]),file=res)
    print("  proposal: %g\n"%prms[p][-1],file=res)

pbloc = []
for p in priors:
  if p in prms:
    pb = p+"_prior: 'lambda %s:stats.norm.logpdf(%s, loc=%g, scale=%g)'"%(p,p,priors[p][0],priors[p][1])
    pbloc +=[pb]
  else:
    print(p,":",file=res)
    if p in latex:
      print("  latex: ",latex[p],file=res)
    print("  prior:\n    dist: norm\n    loc: %g\n    scale: %g"%(priors[p][0],priors[p][1]),file=res)
    print("  proposal: %g\n"%priors[p][-1],file=res)

if pbloc:
  print("prior:",file=res)
  for pb in pbloc:
    print("  "+pb,file=res)

res.close()

