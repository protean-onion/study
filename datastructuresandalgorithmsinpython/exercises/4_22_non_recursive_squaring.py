# coding: utf-8
def non_recursive_power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        z = x
        for i in range(2, n + 1):
            z = z * x
    return z
    
