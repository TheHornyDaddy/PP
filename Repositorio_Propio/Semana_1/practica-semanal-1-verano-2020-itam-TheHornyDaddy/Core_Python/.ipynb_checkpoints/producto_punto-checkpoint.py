def vector(): 
    dim = int(input("Introduzca la dimensión que tendrán los dos vectores: "))
    
    vec1 = []
    vec2 = []
    i = 0
    
    for i in range(dim):
        ent1 = float(input("Introduce la entrada " + " " + str(i+1) + " " + "del primer vector."))
        ent2 = float(input("Introduce la entrada " + " " + str(i+1) + " " + "del segundo vector."))
        print("\n")        
        
        vec1.append(ent1)
        vec2.append(ent2)
        
    print(vec1)
    print(vec2)