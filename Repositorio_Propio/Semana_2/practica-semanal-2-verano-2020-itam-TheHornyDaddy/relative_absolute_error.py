def rae(approx, obj):
    abs_obj = pow(pow(obj,2),1/2)
    abs_ao = pow(pow(approx - obj,2),1/2)
    if(abs_obj > 0 ):
        return abs_ao/abs_obj
    else:
        return abs_ao
