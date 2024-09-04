def addition(list_of_lists):
    sum = 0
    for l in list_of_lists:
        for element in l:
            sum += element

    return sum