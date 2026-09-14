import numpy as np
from scipy import linalg

S = np.array([[6, 1, 2, 0],
              [1, 5, 0, 1],
              [2, 0, 4, 2],
              [0, 1, 2, 3]], dtype=float)

print("S =\n", S)

# i
q, r = linalg.qr(S)
print("\nQ =\n", q)
print("\nR =\n", r)

# ii
u, sigma, vt = linalg.svd(S)
print("\nU =\n", u)
print("\nSigma =\n", sigma)
print("\nV^T =\n", vt)

# iii
b = np.array([7, 3, 5, 4], dtype=float)
x, residuals, rank, sv = linalg.lstsq(S, b)
print("\nx =\n", x)
print("\nrank =", rank)