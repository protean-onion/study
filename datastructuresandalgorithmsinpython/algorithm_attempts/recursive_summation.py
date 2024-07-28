# coding: utf-8
def recursive_summation(S):
#   Recursively return the last value of the input list
#   added to the last value of the same list with the
#   last element omitted till the list has no elements.
    length = len(S)
    if length == 0:
        return 0
    else:
        return S[length - 1] + recursive_summation(S[0:length - 1])
        
