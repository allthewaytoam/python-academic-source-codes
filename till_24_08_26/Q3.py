from scipy import linalg

M = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

print("M =\n", M)

M_T = [list(row) for row in zip(*M)]
print("\nTranspose of M =\n", M_T)

singular_values = linalg.svdvals(M)
rank_M = sum(value > 1e-10 for value in singular_values)
print("\nRank of M =", rank_M)
