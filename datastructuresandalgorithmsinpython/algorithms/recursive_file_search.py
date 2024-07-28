from os.path import getsize, isdir, isfile, join
from os import listdir

# coding: utf-8
def calculate_file_size(target_file):
## Perhaps I am not adding the size of the directory, which--in its os impplementation--does not include the sub-files.
#### https://stackoverflow.com/questions/10404534/os-path-getsize-returns-incorrect-value
    return_size = 0
    
    if isdir(target_file):
        dir_size = getsize(target_file)
        total_directory_size = dir_size
        
        for sub_file in listdir(target_file):
            sub_file_size = calculate_file_size(target_file + "/" + sub_file)
#           total_directory_size += getsize(target_file) + sub_file_size
##          Directory size added len(target_file) + 1 times instead of once
            total_directory_size += sub_file_size
  
        return_size += total_directory_size
        
    elif isfile(target_file):
        return_size += getsize(target_file)
        components = target_file.split("/")
        
    return return_size
    
