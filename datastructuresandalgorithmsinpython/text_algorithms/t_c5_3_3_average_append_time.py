from time import time

def average_append_time(n):
    a = []
    total_time = 0

    for i in range(1, n + 1):
        start = time()
        a.append(0)
        stop = time()
        total_time += stop - start
    
    return total_time / n