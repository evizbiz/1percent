#!/usr/bin/env python

import sys, codecs, json, yfinance

# if we need to sanitize poorly encoded text for tty output:
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)


#tics = "atax diax dsl fof gut hqh hql jta jtd mfd ohi bdcs sdiv slv tpz wfc yyy"
tics = "c wfc"
tics = tics.split(' ')
print(tics)

for t in tics:
  q = yfinance.Ticker(t)
  try:
    info = q.info.items()
    for item in info: print(t,item)
  except: 
    print("failed to get ticker quote for:", t)
  try:
    opts_exp = q.options
    exp = opts_exp[0]
    opt = q.option_chain(exp)
    print(opt.calls, opt.puts)
    #for exp in opts_exp:
      #print(t, exp)
      #opt = q.option_chain(exp)
      #print(opt.calls, opt.puts)
  except: 
    print("failed to get options quote for:", t)


