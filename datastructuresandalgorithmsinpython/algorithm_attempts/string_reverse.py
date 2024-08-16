# coding: utf-8
def reverse(string):
    string = list(string)
    reversed_string = []
    for i in range(len(string) - 1, -1, -1):
        reversed_string.append(string[i])
    return "".join(reversed_string)
    
