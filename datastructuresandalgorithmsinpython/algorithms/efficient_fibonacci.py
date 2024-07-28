# coding: utf-8
def efficient_fibonacci(n):
    l = [1, 1]
    for i in range(2,n):
        l.append(l[i-1] + l[i-2])
    return l[n - 1]
    
