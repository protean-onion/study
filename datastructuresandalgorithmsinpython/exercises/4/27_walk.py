# coding: utf-8
def my_walk(path):
    yields = [(path, [sub_directory for sub_directory in listdir(path) if isdir(join(path, sub_directory))], [sub_file for sub_file in listdir(path) if isfile(join(path, sub_file))])]
    for sub_path in listdir(path):
        if isdir(join(path, sub_path)):
            yields += my_walk(join(path, sub_path))
    return yields
    
