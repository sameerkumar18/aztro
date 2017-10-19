import unittest

from aztro.signs import get_day_based_on_tz


class TestSigns(unittest.TestCase):
    def setUp(self):
        self.tz = 'Asia/Bangkok'

    def test_get_day_based_on_tz_yesterday(self,):
        day = 'yesterday'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)

    def test_get_day_based_on_tz_today(self,):
        day = 'today'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)

    def test_get_day_based_on_tz_tomorrow(self,):
        day = 'tomorrow'
        self.assertEqual(get_day_based_on_tz(day, self.tz), day)
