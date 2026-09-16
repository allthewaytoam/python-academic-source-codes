from scipy import linalg

S = [[6, 1, 2, 0],
     [1, 5, 0, 1],
     [2, 0, 4, 2],
     [0, 1, 2, 3]]

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
b = [7, 3, 5, 4]
x, residuals, rank, sv = linalg.lstsq(S, b)
print("\nx =\n", x)
print("\nrank =", rank)