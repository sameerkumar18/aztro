import requests
day = "today"
sign = "aries"
api = "http://aztro.sameerkumar.website/?sign="+sign+"&day="+day

r = requests.post(api)

print(r)