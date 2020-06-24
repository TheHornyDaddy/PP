def func_fibonacci(n): 
    lista = []
    num1 = 0
    num2 = 1
    if n == 0: 
        lista.append(num1)
        return lista
    elif n == 1: 
        lista.append(num1)
        lista.append(num2)
        return lista
    else: 
        lista.append(num1)
        lista.append(num2)
        for i in range(2,n): 
            fib = num1 + num2
            num1 = num2 
            num2 = fib
            lista.append(fib)
        return lista 