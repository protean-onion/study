# coding: utf-8
def non_recursive_reverse(S):
    start = 0
    stop = len(S) - 1
    while start < stop:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start += 1
        stop -= 1
        
