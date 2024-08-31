# coding: utf-8
def recursive_reverse(l):
    length = len(l)
    recursive_list = []
    if length > 1:
        local_list = [l[-1]]
        local_list.extend(recursive_reverse(l[:-1]))
        recursive_list.extend(local_list)
    else:
        recursive_list.extend([l[0]])
    return recursive_list
    
