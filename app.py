import requests
from flask import Flask, request, redirect, make_response
from flask_cors import CORS
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
import requests


from astrology import horoscope_info
from utils import _setup_debug_logger

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)

logger = _setup_debug_logger(__name__)

signs = {
    "aries": 1,
    "taurus": 2,
    "gemini": 3,
    "cancer": 4,
    "leo": 5,
    "virgo": 6,
    "libra": 7,
    "scorpio": 8,
    "sagittarius": 9,
    "capricorn": 10,
    "aquarius": 11,
    "pisces": 12,
}

days = [
    'today', 'tomorrow', 'yesterday'
]


given_sign = "aries"

URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + \
    str(signs[given_sign])


response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

container = soup.find("p")

print(container.text.strip())

api.add_resource(response, '/')

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
