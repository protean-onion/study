# coding: utf-8
def recursive_min_max(S, start, stop, minimum, maximum):
    if start > stop:
        return minimum, maximum
    else:
        if S[start] > S[maximum]:
            maximum = start
        if S[start] < S[minimum]:
            minimum = start
        if S[stop - 1] > S[maximum]:
            maximum = stop - 1
        if S[stop - 1] < S[minimum]:
            minimum = stop - 1
        return recursive_min_max(S, start + 1, stop - 1, minimum, maximum)
        
