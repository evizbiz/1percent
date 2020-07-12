#!/usr/bin/env python

import requests

tickr = 't' 
url = 'https://option-chain.p.rapidapi.com/straddle/' + tickr

api_hdrs = {
    'x-rapidapi-host': "option-chain.p.rapidapi.com",
    'x-rapidapi-key': "ec866c3dafmsh8ee53350a526aeep1a5cbdjsn2fdaf680b7d7"
    }

response = requests.request("GET", url, headers=api_hdrs)

print(response.text)
