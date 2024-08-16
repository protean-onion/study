# coding: utf-8
def recursive_reverse(string):
    string_list = list(string)
    start = 0
    stop = len(string)
    def reverse(string_list, start, stop):
        if start < stop - 1:
            string_list[start], string_list[stop - 1] = string_list[stop - 1], string_list[start]
            reverse(string_list, start + 1, stop - 1)
    reverse(string_list, start, stop)
    return "".join(string_list)
    
