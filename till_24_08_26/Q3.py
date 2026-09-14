import numpy as np

M = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]], dtype=float)

print("M =\n", M)

M_T = M.T
print("\nTranspose of M =\n", M_T)

rank_M = np.linalg.matrix_rank(M)
print("\nRank of M =", rank_M)