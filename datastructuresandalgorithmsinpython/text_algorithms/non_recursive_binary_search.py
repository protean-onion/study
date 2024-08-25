# coding: utf-8
def non_recursive_binary_search(S, target):
    low = 0
    high = len(S) - 1
    
    while True:
        mid = floor((low + high) / 2)
        try:
            if S[mid] == target:
                return mid
            else:
                if S[mid] > target:
                    high = mid - 1
                elif S[mid] < target:
                    low = mid + 1
            if mid == low or mid == high:
                print("Target is not in list")
                break
        except:
            break
