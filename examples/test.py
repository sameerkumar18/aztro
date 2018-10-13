import requests
day = "today"
sign = "aries"
api_url = "https://aztro.sameerkumar.website/?sign="+sign+"&day="+day

r = requests.post(api_url)

print(r)
