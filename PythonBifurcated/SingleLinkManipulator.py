import numpy as np


def SingleLinkManipulator(curr_state, u):
    J = 1.625103
    m = 0.506
    M0 = 0.434
    L0 = 0.305
    R0 = 0.023
    B0 = 16.25163
    L = 0.0250103
    R = 5.0
    Kt = 0.90
    Kb = 0.90
    g = 9.8
    M = J + m * L0 * L0 / 3.0 + M0 * L0 * L0 + 2 * M0 * R0 * R0 / 5 / Kt
    N = m * L0 * g / 2.0 + M0 * L0 * g / Kt
    B = B0 / Kt

    x1 = curr_state[0, 0]
    x2 = curr_state[0, 1]
    x3 = (u - Kb * x2) / R

    x1dot = x2;
    x2dot = -(N / M) * np.sin(x1) - (B / M) * x2 + (x3 / M);

    dyndot = np.zeros((1, 2));
    dyndot[0, 0] = x1dot;
    dyndot[0, 1] = x2dot;
    return dyndot
