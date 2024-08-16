# coding: utf-8
def recursive_maximum(S, start, stop, maximum_index):
    if start > stop - 1:
        return maximum_index
    else:
        if S[start] > S[maximum_index]:
            maximum_index = start
        if S[stop - 1] > S[maximum_index]:
            maximum_index = stop - 1
        return recursive_maximum(S, start + 1, stop - 1, maximum_index)
        
