# coding: utf-8
def recursive_sum_to_k(S, k, index1, index2):
    print(index1, index2)
    if index1 + 1 <= len(S) and index2 + 1 <= len(S):
        if S[index1] + S[index2] == k:
            return True, index1, S[index1], index2, S[index2]
        else:
            if index1 + 1 <= len(S):
                if index2 + 1 <= len(S):
                    return recursive_sum_to_k(S, k, index1, index2 + 1)
                else:
                    index2 = 0
                    return recursive_sum_to_k(S, k, index1 + 1, index2)
            else:
                return False
                
