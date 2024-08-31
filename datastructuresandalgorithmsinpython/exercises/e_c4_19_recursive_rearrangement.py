# coding: utf-8
def recursive_rearrangement(l, index):
    if len(l) == index + 1:
        return l
    else:
        if l[index] % 2 != 0:
            l.append(l.pop(index))
            return recursive_rearrangement(l, index + 1)
        else:
            return recursive_rearrangement(l, index + 1)
            
