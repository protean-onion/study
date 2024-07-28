# coding: utf-8
def efficient_recursive_fibonacci(n):
    if n == 1:
        return 1, 0
    else:
        f1, f2 = efficient_recursive_fibonacci(n - 1)
        fn = f1 + f2
        return fn, f1
        
        
