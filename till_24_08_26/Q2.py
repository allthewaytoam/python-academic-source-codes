import numpy as np
from scipy import linalg

# a
coeff = np.array([[2, 3],
                   [4, 5]], dtype=float)
const = np.array([8, 14], dtype=float)

sol = linalg.solve(coeff, const)
print("x =", sol[0], " y =", sol[1])

# b
coeff2 = np.array([[1, -1],
                    [1, 1]], dtype=float)
const2 = np.array([1 / 11, 1], dtype=float)

velocity_ratio = linalg.solve(coeff2, const2)
print("velocity of car 1 =", round(velocity_ratio[0], 2), "D units/hr")
print("velocity of car 2 =", round(velocity_ratio[1], 2), "D units/hr")