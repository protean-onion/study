# coding: utf-8
def efficient_power(x, n):
    if n == 0:
        return 1
    else:
        partial = efficient_power(x, n // 2)
        partial_product = partial * partial
        odd_even = n % 2
        if odd_even == 1:
            return partial_product * x
        else:
            return partial_product
            
