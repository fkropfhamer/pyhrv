from unittest import TestCase
import numpy as np

from pyhrv.time_domain import stress_index


class Test(TestCase):
    def test_stress_index(self):
        r = stress_index(np.array([0, 4] * 100))

        assert r == 6.25
