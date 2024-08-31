# coding: utf-8
from t_c5_3_dynamic_array import DynamicArray
from time import time

def tuple_statistics(n_samples):
    def create_array_batch(n_samples, size):
        arrays = []
        for i in range(10):
            array = DynamicArray()
            for j in range(size):
                array.append(0)
            arrays.append(array)
        return arrays

    def time_execute(array, index):
        start = time()
        array.my_add_element("a", index)
        stop = time()
        return stop - start
        
    def time_array_batch(array_batch, index):
        times = 0
        for array in array_batch:
            time = time_execute(array, index)
            times += time
        return times / len(array_batch)
    
    statistical_tuple = []
    for size in range(100):
        for index in range(size):
            array_batch = create_array_batch(n_samples, size)
            average_time = time_array_batch(array_batch, index)
            statistical_tuple.append([size, index, average_time])
    
    return statistical_tuple
    
