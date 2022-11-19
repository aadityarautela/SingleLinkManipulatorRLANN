import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from Quantize import *
from Reward import *
from SingleLinkManipulator import *

X1_BOUND = 10
X2_BOUND = 5
U_BOUND = 10
gamma = 0.99
X1 = np.linspace(0, 1.0, X1_BOUND)
X2 = np.linspace(0, 1.5, X2_BOUND)
N1 = X1.shape[0]
N2 = X2.shape[0]
U = np.linspace(0, 2.5, U_BOUND)
# U = np.linspace(-10, 10, U_BOUND)
policy = np.zeros((N1, N2))
pol = np.zeros((N1, N2))
V = np.zeros((N1, N2))

nextV = np.zeros((N1, N2, U.shape[0]))
print(nextV.shape)
for runs in range(10):
    for i in range(N1):
        for j in range(N2):
            curr_state = np.zeros((1, 2))
            curr_state[0, 0] = X1[i]
            curr_state[0, 1] = X2[j]
            for u in range(10):
                action = U[u];
                dyndot = SingleLinkManipulator(curr_state, action)
                next_state = curr_state + 0.1 * dyndot
                quant_state = Quantize(next_state, X1, X2)
                x1 = int(quant_state[0, 0])
                x2 = int(quant_state[0, 1])
                nextV[i, j, u] = V[x1, x2]
            [Vbest, bestind] = np.max(nextV[i, j, :]), np.argmax(nextV[i, j, :])
            V[i, j] = Reward(X1[i], X2[j]) + gamma * Vbest
            pol[i, j] = U[bestind]

np.savetxt("V.csv", V, delimiter=",")

for i in range(N1):
    for j in range(N2):
        nextV = np.zeros((1, U.shape[0]))
        curr_state = np.zeros((1, 2))
        curr_state[0, 0] = X1[i]
        curr_state[0, 1] = X2[j]
        for u in range(U.shape[0]):
            action = U[u];
            dyndot = SingleLinkManipulator(curr_state, action)
            next_state = curr_state + 0.1 * dyndot
            quant_state = Quantize(next_state, X1, X2)
            x1 = int(quant_state[0, 0])
            x2 = int(quant_state[0, 1])
            nextV[0, u] = V[x1, x2]
        # print(nextV)
        [Vbest, bestind] = np.max(nextV), np.argmax(nextV);
        policy[i, j] = U[bestind];

np.savetxt("policy.csv", policy, delimiter=",")
