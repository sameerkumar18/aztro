import requests
from flask import Flask, request, redirect, make_response
from flask_cors import CORS
from flask_restful import Resource, Api

from astrology import horoscope_info
from utils import _setup_debug_logger

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)

logger = _setup_debug_logger(__name__)

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

days = [
    'today', 'tomorrow', 'yesterday'
]


class API(Resource):
    def get(self):
        # Source: https://github.com/sameerkumar18/aztro-landing-page
        return make_response(
            requests.get('https://cdn.jsdelivr.net/gh/sameerkumar18/aztro-landing-page/index.html').text)

    def post(self):
        sign = request.args['sign'].lower()
        day = request.args.get('day', 'today').lower()
        timezone = request.args.get('tz')
        try:
            if (sign not in signs) or (day not in days):
                raise Exception('Wrong sign or day passed. Please refer https://aztro.readthedocs.io/en/latest/ ')

            response = horoscope_info(sign=sign, day=day, tz=timezone)
            return response, 200
        except Exception as e:
            logger.error("{}".format(e))
            return {'message': str(e)}, 400


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=302)


api.add_resource(API, '/')

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
