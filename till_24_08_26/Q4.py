from scipy import linalg

Q = [[4, 1, 2, 0],
     [1, 3, 0, 1],
     [2, 0, 5, 2],
     [0, 1, 2, 6]]

print("Q =\n", Q)

# a
eigenvalues, eigenvectors = linalg.eig(Q)
print("\nEigenvalues =\n", eigenvalues)
print("\nEigenvectors =\n", eigenvectors)

# b
P, L, U = linalg.lu(Q)
print("\nP =\n", P)
print("\nL =\n", L)
print("\nU =\n", U)