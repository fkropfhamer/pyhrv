from unittest import TestCase
import numpy as np

from pyhrv.detrend import moving_avg, smoothness_priors


class Test(TestCase):
    def test_detrend_moving_avg_with_ones(self):
        r = moving_avg(np.ones(100))

        assert np.isclose(r, np.ones(100)).all()

    def test_detrend_smoothness_priors_with_ones(self):
        r = smoothness_priors(np.ones(100))

        assert np.isclose(r, np.zeros(100)).all()
