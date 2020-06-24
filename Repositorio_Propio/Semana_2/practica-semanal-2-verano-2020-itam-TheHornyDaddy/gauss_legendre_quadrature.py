def GLf(f,a,b,n): #GLf: Gauss-Legendre quadrature for f
    """
    Compute numerical approximation using quadrature Gauss-Legendre.
    Weights and nodes are obtained with table for n=0,1,2,3,4
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    
    if(n == 0):
        w = [2]
        x = [0]
    
    elif(n == 1):
        w = [1,1]
        x = [-pow(1/3,1/2),pow(1/3,1/2)]
        
    elif(n == 2):
        w = [5/9,8/9,5/9]
        x = [-pow(3/5,1/2),0,pow(3/5,1/2)]
        
    elif(n == 3):
        w = [0.347855,0.652145,0.652145,0.347855]
        x = [-0.861136,-0.339981,0.339981,0.861136]
        
    elif(n == 4):
        w = [0.236927,0.478629,0.568889,0.478629,0.236927]
        x = [-0.90618,-0.538469,0,0.538469,0.90618]
    
    else:
        print("Error")
    
    sum_aux = 0
    
    for i in range(0,n+1):
        sum_aux += w[i]*f(0.5*((b-a)*x[i]+a+b))
    sum_res = ((b-a)/2)*sum_aux
                          
    return sum_res
