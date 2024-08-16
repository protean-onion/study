# coding: utf-8
def recursive_sum_to_k(S, k, index1 = 0, index2 = 0):
    if index1 + 1 <= len(S) and index2 + 1 <= len(S):
        if S[index1] + S[index2] == k:
            return True, index1, S[index1], index2, S[index2]
        else:
            return recursive_sum_to_k(S, k, index1, index2 + 1)
    else:
        if index1 + 1 <= len(S)  and index2 + 1 > len(S):
            index2 = 0
            return recursive_sum_to_k(S, k, index1 + 1, index2)
        elif index1 + 1 > len(S):
            return False
            
