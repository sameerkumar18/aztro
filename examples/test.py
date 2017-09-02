import requests
day = "today"
sign = "aries"
api = "http://aztro.herokuapp.com?sign="+sign+"&day="+day

r = requests.post(api)

print r