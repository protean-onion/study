# coding: utf-8
def recursive_reverse(l):
    print(l)
    length = len(l)
    recursive_list = []
    if length > 1:
        print(l)
        last_element = l[-1]
        recursive_list.extend([last_element, recursive_reverse(l[:-1])])
        return recursive_list
    else:
        return [l[0]]
        
