# coding: utf-8
def tick_counts(tick_length):
    l = [[1,2,1]]
    if tick_length < 3:
        return l[0]
    if tick_length >= 3:
        for i in range(3, tick_length + 1):
            temp = []
            temp.extend(l[i - 3])
            temp.extend(i)
            temp.extend(l[i - 3])
            l.append(a)
            
def tick_counts(tick_length):
    l = [[1,2,1]]
    if tick_length < 3:
        return l[0]
    if tick_length >= 3:
        for i in range(3, tick_length + 1):
            temp = []
            temp.extend(l[i - 3])
            temp.extend(i)
            temp.extend(l[i - 3])
            l.append(a)
    return l[-1]
    
tick_counts(3)
def tick_counts(tick_length):
    l = [[1,2,1]]
    if tick_length < 3:
        return l[0]
    if tick_length >= 3:
        for i in range(3, tick_length + 1):
            temp = []
            temp.extend(l[i - 3])
            temp.extend([i])
            temp.extend(l[i - 3])
            l.append(a)
    return l[-1]
    
tick_counts(3)
def tick_counts(tick_length):
    l = [[1,2,1]]
    if tick_length < 3:
        return l[0]
    if tick_length >= 3:
        for i in range(3, tick_length + 1):
            temp = []
            temp.extend(l[i - 3])
            temp.extend([i])
            temp.extend(l[i - 3])
            l.append(temp)
    return l[-1]
    
tick_counts(3)
tick_counts(10)
a = tick_counts(10)
for i in range(len(a)):
    print("-" * i)
    
a
for i in range(len(a)):
    print("-" * i + "\n")
    
len(a)
a = tick_counts(3)
a
a = tick_counts(4)
a
def draw_ticks(tick_counts):
    for i in range(len(tick_counts)):
        print("-" * i)
        
a = tick_counts(3)
a
def draw_ticks(tick_counts):
    for i in range(len(tick_counts)):
        print("-" * tick_counts[i])
        
draw_ticks(a)
get_ipython().run_line_magic('save', '~/coding/py')
