# coding: utf-8
def recursive_multiplication(m, n):
    if n == 0:
        return 0
    else:
        return m + recursive_multiplication(m, n - 1)
        
