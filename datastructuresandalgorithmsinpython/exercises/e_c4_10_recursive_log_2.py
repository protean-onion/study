# coding: utf-8
def recursive_log_2(n):
    if n == 0:
        pass
    elif n == 1:
        return 0
    else:
        return 1 + recursive_log_2(n // 2)
        
