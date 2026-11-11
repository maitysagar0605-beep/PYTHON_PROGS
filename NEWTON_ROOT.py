from scipy.optimize import newton
f= lambda x: x**3 - 2*x - 5
df= lambda x: 3*x**2 - 2
root = newton(f, x0=2, fprime=df)
print("Root found:", root)