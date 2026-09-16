from scipy import linalg

# a
coeff = [[2, 3],
         [4, 5]]
const = [8, 14]

sol = linalg.solve(coeff, const)
print("x =", sol[0], " y =", sol[1])

# b
coeff2 = [[1, -1],
          [1, 1]]
const2 = [1 / 11, 1]

velocity_ratio = linalg.solve(coeff2, const2)
print("velocity of car 1 =", round(velocity_ratio[0], 2), "D units/hr")
print("velocity of car 2 =", round(velocity_ratio[1], 2), "D units/hr")