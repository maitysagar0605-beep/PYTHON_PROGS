def bisection_method(func, a, b, error_accept):
    """
    Solves for an unknown root of a non-linear function given the function string,
    initial root boundaries, and an acceptable level of error.

    Parameters:
    -----------
    func : str
        The user-defined mathematical expression using variable 'x'.
    a : float or int
        The initial lower root boundary.
    b : float or int
        The initial upper root boundary.
    error_accept : float
        The acceptable level of tolerance/error.

    Returns:
    --------
    tuple
        (a, b, error) at the final iteration.
    """
    def f(x):
        return eval(func)

    # Initial bracket check
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs. The bisection method cannot guarantee a root.")

    error = abs(b - a)

    while error > error_accept:
        c = (b + a) / 2
        fc = f(c)

        if fc == 0:
            a = b = c
            error = 0.0
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        error = abs(b - a)

    print(f"The final error is: {error}")
    print(f"The final lower boundary 'a' is {a} and upper boundary 'b' is {b}")
    return a, b, error


# Example Call with corrected function string ("3*x" instead of "3x")
bisection_method("(4 * x**3) + 3*x - 3", 0, 1, 0.05)
