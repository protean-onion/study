# coding: utf-8
def recursive_swap_reverse(l):
    length = len(l)
    reversed_list = []
    
    if length > 1:
        first_element = l[0]
        last_element = l[-1]
        middle_elements = l[1:-1]

        reversed_list.extend([last_element])
        reversed_list.extend(recursive_swap_reverse(middle_elements))
        reversed_list.extend([first_element])
    elif length == 1:
        reversed_list.append(l[0])
    else:
        pass
    
    return reversed_list
    
