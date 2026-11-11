import numpy as np

def system_newton(F, J, x0, tol=1e-7, max_iter=100):
    """
    Solves a system of non-linear equations F(x) = 0 using Newton's Method.

    Parameters:
        F        : Function returning a 1D numpy array of the equations [f1, f2, ...].
        J        : Function returning a 2D numpy array of the Jacobian matrix.
        x0       : Initial guess (numpy array or list).
        tol      : Tolerance for convergence.
        max_iter : Maximum number of iterations.

    Returns:
        numpy.ndarray: The root vector.
    """
    x = np.array(x0, dtype=float)

    for i in range(1, max_iter + 1):
        F_val = F(x)
        J_val = J(x)

        # Solve J * delta_x = -F_val for delta_x
        try:
            delta_x = np.linalg.solve(J_val, -F_val)
        except np.linalg.LinAlgError:
            raise ValueError("Jacobian matrix is singular at current step. Newton's method fails.")

        x_next = x + delta_x

        # Calculate error (Euclidean norm of the step vector)
        err = np.linalg.norm(delta_x)
        print(f"Iteration {i}: x = {x_next}, error = {err:.2e}")

        if err < tol:
            print(f"\nConverged in {i} iterations.")
            return x_next

        x = x_next

    raise ValueError("Maximum iterations reached without convergence.")


# --- Define System and Jacobian ---

# System of equations vector F(x, y)
def F(V):
    x, y = V
    f1 = x**2 + y**2 - 4
    f2 = np.exp(x) + y - 1
    return np.array([f1, f2])

# Jacobian Matrix J(x, y) = [[df1/dx, df1/dy], [df2/dx, df2/dy]]
def J(V):
    x, y = V
    return np.array([
        [2*x,       2*y],
        [np.exp(x), 1.0]
    ])

print("Solving the system of equations:")
print("1) x^2 + y^2 - 4 = 0")   
print("2) e^x + y - 1 = 0")

# Initial guess
x0 = [1.5, 1.5]

# Run the algorithm
root = system_newton(F, J, x0)
print(f"\nSolution vector: x = {root[0]:.6f}, y = {root[1]:.6f}")