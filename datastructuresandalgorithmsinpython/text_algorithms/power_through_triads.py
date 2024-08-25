# coding: utf-8
def power_through_triads(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == 2:
        return x * x
    else:
        partial = power_through_triads(x, n // 3)
        partial_triad = partial * partial * partial
        remainder = n % 3
        if remainder == 0:
            return partial_triad
        elif remainder == 1:
            return partial_triad * x
        else:
            return partial_triad * x * x
            
