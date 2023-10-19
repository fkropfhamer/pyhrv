import numpy as np

from pyhrv.utils import std


def detrend_moving_avg():
    return True


def detrend_advanced():
    return std(np.ones(100))
