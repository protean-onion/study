# coding: utf-8
def recursive_harmonic_series(n):
    if n == 1:
        return 1
    else:
        return 1 / n + recursive_harmonic_series(n - 1)
        
