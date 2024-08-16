# coding: utf-8
def recursive_rearrangement(l):
    even = []
    odd = []
    result = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])
    result.extend(even)
    result.extend(odd)
    return result
    
