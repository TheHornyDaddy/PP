def Tcf(f,a,b,n): #Tcf: composite trapezoidal method for f
    """
    Compute numerical approximation using trapezoidal method in 
    an interval.
    Nodes are generated via formula: x_i = a+ih_hat for i=0,1,...,n and h_hat=(b-a)/n
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    h_hat = (b-a)/n
    sum_res = 0
    i = 0
    for i in np.arange(n-1):
        x = a + i*h_hat
        sum_res += f(x)
    T = (h_hat/2)*(f(a) + f(b) + 2*sum_res)
    return T