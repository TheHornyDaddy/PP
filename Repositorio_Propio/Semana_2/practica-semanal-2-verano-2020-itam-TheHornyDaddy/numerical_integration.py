<<<<<<< HEAD
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
    for i in range(0,n-1):
        x = a + i*h_hat
        sum_res += f(x)
    T = (h_hat/2)*(f(a) + f(b) + 2*sum_res)
    return T

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
=======
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
    for i in range(0,n-1):
        x = a + i*h_hat
        sum_res += f(x)
    T = (h_hat/2)*(f(a) + f(b) + 2*sum_res)
    return T

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
>>>>>>> 481075011255c95a2504b921d57f992c81345c4b
