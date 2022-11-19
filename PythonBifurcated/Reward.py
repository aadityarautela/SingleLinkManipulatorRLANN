import numpy as np


def Reward(x1, x2):
    return -np.abs(x1 - np.pi / 6.0) - np.abs(x2)
