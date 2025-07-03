import numpy as np
from scipy.optimize import brentq
import sympy as sp
from sympy import symbols, sin, cos, exp, log, pi, sqrt

def find_roots(func, a=0, b=10, steps=1000, atol=1e-10, variable=None):
    """
    Finds all roots of a function in the interval [a, b].
    
    Parameters:
        func (callable or sympy expression): The function to find roots for.
        a, b (float): The interval to search (default: [0, 10]).
        steps (int): Number of subintervals to check (default: 1000).
        atol (float): Tolerance to filter out duplicate roots (default: 1e-10).
        variable (sympy.Symbol): Variable to use if func is sympy expression (auto-detected if None).
    
    Returns:
        List of roots found within the interval.
    """
    
    # Handle SymPy expressions
    if hasattr(func, 'free_symbols'):  # It's a SymPy expression
        if variable is None:
            # Auto-detect variable
            free_symbols = func.free_symbols
            if len(free_symbols) == 1:
                variable = list(free_symbols)[0]
            elif len(free_symbols) == 0:
                raise ValueError("Expression has no variables")
            else:
                raise ValueError(f"Expression has multiple variables: {free_symbols}. "
                               f"Please specify which one to use with the 'variable' parameter.")
        
        # Convert SymPy expression to numerical function
        numerical_func = sp.lambdify(variable, func, 'numpy')
    else:
        # It's already a callable function
        numerical_func = func
    
    # Create array of x values
    x = np.linspace(a, b, steps)
    roots = []
    
    for i in range(len(x) - 1):
        x0, x1 = x[i], x[i + 1]
        
        try:
            y0, y1 = numerical_func(x0), numerical_func(x1)
            
            # Check for sign change (indicating a root)
            if np.sign(y0) != np.sign(y1):
                try:
                    root = brentq(numerical_func, x0, x1)
                    # Filter out duplicate roots
                    if not any(np.isclose(root, r, atol=atol) for r in roots):
                        roots.append(root)
                except ValueError:
                    pass  # Skip subintervals where brentq fails
        except (ValueError, ZeroDivisionError, OverflowError):
            # Skip points where function evaluation fails
            continue
    
    return sorted(roots)


def verify_roots(func, roots, variable=None, tolerance=1e-8):
    """
    Verify that the found roots are actually roots of the function.
    
    Parameters:
        func: SymPy expression or callable function
        roots: List of root values to verify
        variable: SymPy symbol (for SymPy expressions)
        tolerance: Maximum allowed function value at root
    
    Returns:
        List of (root, function_value) tuples
    """
    if hasattr(func, 'free_symbols'):  # SymPy expression
        if variable is None:
            variable = list(func.free_symbols)[0]
        numerical_func = sp.lambdify(variable, func, 'numpy')
    else:
        numerical_func = func
    
    verification = []
    for root in roots:
        try:
            func_value = numerical_func(root)
            verification.append((root, func_value))
            if abs(func_value) > tolerance:
                print(f"Warning: Root {root:.6f} has function value {func_value:.2e}")
        except:
            verification.append((root, float('nan')))
    
    return verification


# Example usage
if __name__ == "__main__":
    # Define variable
    x = symbols('x')
    
    # Transcendental equation example
    expr = x * cos(x) - 2
    roots = find_roots(expr, a=-10, b=10, steps=2000)
    print(f"Roots of x*sin(x) - 2 = 0: {[f'{r:.6f}' for r in roots]}")
    
    # Verify roots
    verification = verify_roots(expr, roots, x)
    print("Verification:")
    for root, value in verification:
        print(f"  f({root:.6f}) = {value:.2e}")