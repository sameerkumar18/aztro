from .. import app as aztro
import unittest
import json


class AztroTestCase(unittest.TestCase):
    signs = [
        'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
        'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
    ]

    days = [
        'today', 'tomorrow', 'yesterday'
    ]

    def setUp(self):
        aztro.app.testing = True
        self.app = aztro.app.test_client()

    def assertAztroResponse(self, response):
        dict_keys = [
            'current_date', 'compatibility', 'lucky_time', 'lucky_number',
            'color', 'date_range', 'mood', 'description'
        ]

        response_data = json.loads(response.data)

        for dict_key in dict_keys:
            self.assertTrue(
                dict_key in response_data,
                'Key {} not in response'.format(dict_key)
            )
        self.assertEqual(response.status_code, 200)

    def test_landing_page(self):
        response = self.app.get('/', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        response = self.app.get('/notfound', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    def test_api(self):
        for sign in self.signs:
            for day in self.days:
                url = '/?sign={sign}&day={day}'.format(sign=sign, day=day)
                response = self.app.post(url)

                self.assertAztroResponse(response)
