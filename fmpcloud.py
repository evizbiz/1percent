#!/usr/bin/env python
from pyfmpcloud import settings
from pyfmpcloud import stock_time_series as sts

fmpc_key = '59905dc223dae03bb6d76fc0c201433c'

settings.set_apikey(fmpc_key)

tickr = 'AAPL'

rtq = sts.real_time_quote(tickr)

print(rtq)

