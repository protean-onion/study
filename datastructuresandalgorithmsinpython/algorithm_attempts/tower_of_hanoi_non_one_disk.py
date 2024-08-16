# coding: utf-8
def tower_of_hanoi(n):
    a = [i for i in range(n, 0, -1)]
    b = []
    c = []
    def solve(a, b, c):
        if len(a) == len(b) == 0:
            print("Solved!")
            return a, b, c
        elif len(b) == len(c) == 0:
            b.append(a.pop())
            c.append(a.pop())
            return solve(a, b, c)
        else:
            if b[0] > c[0]:
                b.extend(c)
                for _ in range(len(c)):
                    c.pop()
                try:
                    c.append(a.pop())
                except:
                    return a, b, c
            elif c[0] > b[0]:
                c.extend(b)
                for _ in range(len(b)):
                    b.pop()
                try:
                    b.append(a.pop())
                except:
                    return a, b, c
            return solve(a, b, c)
    return solve(a, b, c)
    
