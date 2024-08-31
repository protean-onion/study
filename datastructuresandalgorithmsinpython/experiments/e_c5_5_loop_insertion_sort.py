# coding: utf-8
def loop_insertion_sort(data):
    for i in range(len(data)):
        current = data[i]
        
        index_count = 0
        for j in range(i, -1, -1):
            if data[j] > current:
                index_count += 1
                continue
            else:
                pass
                
        for k in range(i, i - index_count, - 1):
            data[k] = data[k - 1]
            
        data[i - index_count] = current
        
