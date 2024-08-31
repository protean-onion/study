# coding: utf-8
def insertion_sort_in_batches(data):
    # This is an O(n^2) time-complexity algorithm!
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                
