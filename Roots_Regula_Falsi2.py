# Define the equation f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2


# 1. Regula-Falsi Method
def regula_falsi(a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses.")
        return

    c = a
    while abs(f(c)) > tol:
        # Formula
        c = b - (f(b) * (b - a)) / (f(b) - f(a))

        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Regula-Falsi Root:", round(c, 4))


# 2. Secant Method
def secant(x0, x1, tol=0.0001):
    while abs(f(x1)) > tol:
        # Formula
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        # Shift points
        x0 = x1
        x1 = x2

    print("Secant Root:", round(x1, 4))


# Run both methods with initial guesses 1 and 2
regula_falsi(1, 2)
secant(1, 2)
