#!/usr/bin/env python

import sys, codecs, datetime, json
print(sys.version)

import codecs, datetime, json
import yfinance as yf

# if we need to sanitize poorly encoded text for tty output:
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)


def yf_close(tics, week):
  print(tics)
  data = yf.download(tics, week.start, week.end, group_by="ticker")
  for t in tics:
    t = t.upper()
    print(t, 'close:', data[t]['Close'])

  return data

def yf_options(tics):
  print(tics)
  tdict = {}
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
      print(exp, opt.calls, opt.puts)
      tdict[t] = { exp, opt }
      #for exp in opts_exp:
        #print(t, exp)
        #opt = q.option_chain(exp)
        #print(opt.calls, opt.puts)
    except: 
      print("failed to get options quote for:", t)

  return tdict

class Week:
  def __init__(self, start='2020-07-06', end='2020-07-10'):
    self.start = start ; self.end = end

if __name__ == '__main__':
  #tics = "atax diax dsl fof gut hqh hql jta jtd mfd ohi bdcs sdiv slv tpz wfc yyy"
  tics = "c wfc"
  tics = tics.split(' ')
  week = Week()
  #week = new week('2020-07-06', '2020-07-10')
  yf_close(tics, week)

