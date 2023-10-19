from unittest import TestCase

from pyhrv.detrend import detrend_moving_avg, detrend_advanced


class Test(TestCase):
    def test_detrend_moving_avg(self):
        r = detrend_moving_avg()
        assert r

    def test_detrend_advanced(self):
        assert detrend_advanced() == 1