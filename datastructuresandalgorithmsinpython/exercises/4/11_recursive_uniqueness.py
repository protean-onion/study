# coding: utf-8
def recursive_uniqueness(S, index, check_list):
    def uniqueness(S, index, check_list):
        if S[index] not in check_list:
            check_list.append(S[index])
            return True
        else:
            return False
            
    if len(S) >= index + 1:
        if uniqueness(S, index, check_list):
            return recursive_uniqueness(S, index + 1, check_list)
        else:
            return False
    else:
        return True
        
