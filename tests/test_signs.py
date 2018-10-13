import unittest

from astrology import get_day_based_on_tz
from astrology import SERVER_TIMEZONE


class TestSigns(unittest.TestCase):
    def setUp(self):
        self.tz = SERVER_TIMEZONE

    def test_get_day_based_on_tz_yesterday(self,):
        day = 'yesterday'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)

    def test_get_day_based_on_tz_today(self,):
        day = 'today'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)

    def test_get_day_based_on_tz_tomorrow(self,):
        day = 'tomorrow'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)
