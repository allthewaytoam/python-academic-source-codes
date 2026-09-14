import numpy as np

A = np.array([[4, 7, 2],
              [3, 6, 1],
              [2, 5, 3]], dtype=float)

B = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]], dtype=float)

print("A =\n", A)
print("B =\n", B)

# i
A_inv = np.linalg.inv(A)
print("\nInverse of A =\n", A_inv)

# ii
det_B = np.linalg.det(B)
print("\nDeterminant of B =", det_B)

# iii
ic = np.round(A @ A_inv, decimals=10)
ic[np.isclose(ic, 0)] = 0
print("\nA . A_inv =\n", ic)
print("\nA . A_inv is identity:", np.allclose(A @ A_inv, np.eye(A.shape[0])))