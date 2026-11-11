from scipy.optimize import root
import numpy as np

def F(V):
    x, y = V
    return [x**2 + y**2 - 4, np.exp(x) + y - 1]

print("Solving the system of equations:")
print("1) x^2 + y^2 - 4 = 0")   
print("2) e^x + y - 1 = 0")

sol = root(F, x0=[1.5, 1.5], method='hybr')
print("Root:", sol.x)