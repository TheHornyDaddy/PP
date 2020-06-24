def punto(vec1,vec2): 
    if len(vec1) == len(vec2):
        i = 0
        sum = 0

        for i in range(len(vec1)):
            sum += vec1[i] + vec2[i]

        print(sum)
    
    else:
        print("Los vectores no son de la misma dimensión:")