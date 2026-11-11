def newton_method(f, df, x0, tol=1e-7, max_iter=100):
    x = x0
    for _ in range(max_iter):
        df_val = df(x)
        if df_val == 0:
            raise ZeroDivisionError("Derivative is zero.")
        x_next = x - f(x) / df_val
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    raise ValueError("Did not converge.")

# Example usage (No scipy required)
f = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2

print("Finding root of the function f(x) = x^3 - 2x - 5 using Newton's method.")
root = newton_method(f, df, x0=2.0)
print(f"Root: {root:.7f}")