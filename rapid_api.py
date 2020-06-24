import requests

url = "https://option-chain.p.rapidapi.com/straddle/msft"

headers = {
    'x-rapidapi-host': "option-chain.p.rapidapi.com",
    'x-rapidapi-key': "ec866c3dafmsh8ee53350a526aeep1a5cbdjsn2fdaf680b7d7"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
