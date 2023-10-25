import numpy as np
from scipy.sparse import spdiags


def moving_avg(rr, window_size=25):
    return rr


def smoothness_priors(rr, l=20):
    t = len(rr)
    i = np.identity(t)
    d2 = spdiags(np.array([np.ones(t), np.repeat(-2, t), np.ones(t)]), np.array([0, 1, 2]), t - 2, t).toarray()
    z_stat1 = i - np.linalg.inv(i + l ** 2 * d2.T @ d2)

    return z_stat1 @ rr
