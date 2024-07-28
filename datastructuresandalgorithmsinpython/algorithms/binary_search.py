# coding: utf-8
def binary_search(S, target):
    low = 0
    high = len(S) - 1
    
    def recursion(S, target, low, high):
        mid = int((low + high) / 2)
        if S[mid] == target:
            return mid
        elif low == mid or high == mid:
            return "Target not in set"
        elif S[mid] < target:
            low = mid + 1
        elif S[mid] > target:
            high = mid - 1
        elif low == mid or high == mid:
            return "Target not in set"
        return recursion(S, target, low, high)
    return recursion(S, target, low, high)
    
