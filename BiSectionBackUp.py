import math

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function f(x) = 0 within interval [a, b] using the Bisection Method.
    
    Parameters:
        f        : The objective function f(x)
        a, b     : Lower and upper bounds of the interval
        tol      : Tolerance/accuracy stopping criteria (default: 1e-6)
        max_iter : Maximum number of iterations (default: 100)
    
    Returns:
        float : Estimated root of the equation
    """
    # Step 1: Check if the initial interval is valid (f(a) and f(b) must have opposite signs)
    if f(a) * f(b) >= 0:
        print("Error: Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    print(f"\n{'Iter':^6}|{'a':^12}|{'b':^12}|{'c (Root)':^12}|{'f(c)':^14}")
    print("-" * 60)
    
    # Step 2: Iterative bisection loop
    for iteration in range(1, max_iter + 1):
        # Calculate midpoint
        c = (a + b) / 2.0
        fc = f(c)
        
        # Print current iteration details
        print(f"{iteration:^6}|{a:^12.6f}|{b:^12.6f}|{c:^12.6f}|{fc:^14.6e}")
        
        # Check if the root is found within the specified tolerance
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            print("-" * 60)
            print(f"Root successfully found after {iteration} iterations.")
            return c
        
        # Update the interval based on intermediate value theorem
        if f(a) * fc < 0:
            b = c  # Root lies in [a, c]
        else:
            a = c  # Root lies in [c, b]
            
    print("-" * 60)
    print("Warning: Maximum iterations reached without reaching desired tolerance.")
    return c


# Example usage: Solving f(x) = x^3 - x - 2 = 0
if __name__ == "__main__":
    # Define the objective function
    def f(x):
        return x**3 - x - 2

    # Initial interval [a, b] and parameters
    a_initial = 1.0
    b_initial = 2.0
    tolerance = 1e-5

    print("=== BISECTION METHOD ===")
    print(f"Solving equation: f(x) = x^3 - x - 2")
    print(f"Initial interval: [{a_initial}, {b_initial}]")

    root = bisection_method(f, a_initial, b_initial, tol=tolerance)
    
    if root is not None:
        print(f"\nApproximate Root = {root:.6f}")
        print(f"Verification: f({root:.6f}) = {f(root):.6e}")