import numpy as np

INF = 100000


def Quantize(state, X1, X2):
    dist1 = INF
    dist2 = INF
    retval = np.zeros((1, 2))
    for x1 in X1:
        if np.abs(state[0, 0] - x1) < dist1:
            retval[0, 0] = x1
            dist1 = np.abs(state[0, 0] - x1)
    for x2 in X2:
        if np.abs(state[0, 1] - x2) < dist2:
            retval[0, 1] = x2
            dist2 = np.abs(state[0, 1] - x2)
    return retval
