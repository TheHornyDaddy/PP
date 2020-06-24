def sda(f,x,h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate first derivative of function.
    Args:
        f (function): function definition.
        x (float): point where first derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        ddfa (float): approximation to first_derivative.
    """
    ddfa = (f(x + 2*h) - 2*f(x + h) + f(x))/(pow(h,2))
    
    return ddfa
