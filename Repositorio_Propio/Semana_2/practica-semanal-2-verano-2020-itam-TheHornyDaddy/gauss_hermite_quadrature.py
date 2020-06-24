def GHf(f,mu, sigma): #GHf: Gauss-Hermite quadrature for f
    """
    Compute numerical approximation using quadrature Gauss-Hermite.
    Weights and nodes are obtained with table in Kiusalaas for n=6
    Args:
        f (function): function expression of integrand
        mu (float): mean
        sigma (float): standard deviation
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    aux = [[-2.35060497, -1.33584907, -0.43607741,  0.43607741,  1.33584907,
          2.35060497],
          [0.00453001, 0.15706732, 0.7246296 , 0.7246296 , 0.15706732,
          0.00453001]]
    x = []
    w = []

    for i in range(0,6):
        x.append(aux[0][i])
        w.append(aux[1][i])
        
    sum_res = 0
        
    for i in range(0,6):
        sum_res += w[i]*f(x[i]*pow(2*sigma**2,1/2) + mu)*pow(3.14159265358979323846,-1/2)
    
    return sum_res
