def f(x):
    """Define the function f(x) = 0 here."""
    return x**3 - x - 2


def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs for Regula-Falsi.")
        return None

    print("\n--- Regula-Falsi (False Position) Method ---")
    print(
        f"{'Iter':<6} {'a':<12} {'b':<12} {'c (Root)':<14} {'f(c)':<14} {'Error':<12}"
    )
    print("-" * 72)

    c_prev = a
    for i in range(1, max_iter + 1):
        # False position formula
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        fc = f(c)
        error = abs(c - c_prev)

        print(
            f"{i:<6} {a:<12.6f} {b:<12.6f} {c:<14.6f} {fc:<14.6e} {error:<12.6e}"
        )

        # Check stopping criteria
        if abs(fc) < tol or (i > 1 and error < tol):
            print(f"\nConverged to root: {c:.6f} in {i} iterations.")
            return c

        # Update the bracketing interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        c_prev = c

    print("\nMaximum iterations reached without full convergence.")
    return c


def secant_method(x0, x1, tol=1e-6, max_iter=100):
    print("\n--- Secant Method ---")
    print(
        f"{'Iter':<6} {'x0':<12} {'x1':<12} {'x2 (Root)':<14} {'f(x2)':<14} {'Error':<12}"
    )
    print("-" * 72)

    for i in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)

        if f1 - f0 == 0:
            print("Error: Division by zero encountered.")
            return None

        # Secant formula
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        fx2 = f(x2)
        error = abs(x2 - x1)

        print(
            f"{i:<6} {x0:<12.6f} {x1:<12.6f} {x2:<14.6f} {fx2:<14.6e} {error:<12.6e}"
        )

        # Check stopping criteria
        if abs(fx2) < tol or error < tol:
            print(f"\nConverged to root: {x2:.6f} in {i} iterations.")
            return x2

        # Shift points forward
        x0, x1 = x1, x2

    print("\nMaximum iterations reached without full convergence.")
    return x2


if __name__ == "__main__":
    # Initial interval / guesses for f(x) = x^3 - x - 2
    # Since f(1) = -2 and f(2) = 4, a root lies in [1, 2]
    a, b = 1.0, 2.0
    tolerance = 1e-6

    regula_falsi(a, b, tol=tolerance)
    secant_method(a, b, tol=tolerance)