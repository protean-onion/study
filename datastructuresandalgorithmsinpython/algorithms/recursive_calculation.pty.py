# coding: utf-8
def recursive_calculation(path):
    total_size = 0
    if isdir(path) == False:
        total_size += getsize(path)
    else:
        total_size += getsize(path)
        for file in listdir(path):
            total_size += recursive_calculation(path + "/" + file)
    return total_size
    
