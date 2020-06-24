#!/bin/bash

export PAGER=more
export PYTHONIOENCODING=UTF-8

time python -c 'import yfinance; q = yfinance.Ticker("c") ; print(q.info)'|sed 's/,/\n/g' 
time python -c 'import yfinance; q = yfinance.Ticker("wfc") ; print(q.info)'|sed 's/,/\n/g' 
time python -c 'import yfinance; q = yfinance.Ticker("slv") ; print(q.info)'|sed 's/,/\n/g' 
#time python -c 'import yfinance; slv = yfinance.Ticker("slv") ; print(slv.info)'|sed 's/,/\n/g' | egrep -i 'bid|ask|shortname'

