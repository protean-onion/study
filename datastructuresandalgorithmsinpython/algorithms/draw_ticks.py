# coding: utf-8
def draw_ticks(center_length):
    l = [[1]]
    for i in range(2, center_length + 1):
        temp = []
        temp.extend(l[i - 2])
        temp.extend([i])
        temp.extend(l[i - 2])
        l.append(temp)
    for i in l[-1]:
        print("-" * i)
        
    
