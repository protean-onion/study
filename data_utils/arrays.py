from time import time
from random import randint

def incremental_random_arrays(value_range, size, n):
    
    pass

def random_array_batches(value_range = 100, size = 100, n = 100):
    return [[randint(0, value_range) for i in range(size)] for i in range(n)]

def time_array_func(func, array):
    start = time()
    func(array)
    stop = time()
    return stop - start

def time_array_batch(func, array_of_arrays):
    return [time_array_func(func, array) for array in array_of_arrays]

def time_random_array_batch(func, value_range = 100, size = 100, n = 100):
    array_of_arrays = random_array_batches(value_range, size, n)
    return time_array_batch(func, array_of_arrays)
