#! /usr/bin/python3

def detect_repetition_fast(array):
    stripped = set(array)
    counts = {}
    for integer in stripped:
        counts[integer] = 0

    for integer in array:
        counts[integer] += 1
    
    for integer_key in counts.keys():
        if counts[integer_key] == 2:
            print("Found it! It is " + str(integer_key))
            break

def detect_repetition_1(array):
    for i in range(len(array)):
        if array[i] in array[i + 1:]:
            print("The repeated element is " + str(array[i]) + ".")
            break
        
def detect_repetition_recursive(array):
    if len(array) > 1:
        if array[0] in array[1:]:
            print("The repeated integer is " + str(array[0]))
        else:
            detect_repetition_recursive(array[1:len(array) // 2])
            detect_repetition_recursive(array[len(array) // 2:])