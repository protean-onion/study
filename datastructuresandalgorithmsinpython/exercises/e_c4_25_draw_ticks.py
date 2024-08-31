# coding: utf-8
def draw_ticks(n):
    ticks = [["-"]]
    for i in range(2, n + 1):
        ticks.append(ticks[-1] + ["-" * i] + ticks[-1])
    if n == 0:
        return
    else:
        for line in ticks[-1]:
            print(line)
            
