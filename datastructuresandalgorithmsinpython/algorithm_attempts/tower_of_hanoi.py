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
            c.append(a.pop())
            b.append(a.pop())
            return solve(a, b, c)
        else:
            if b[0] > c[0]:
                for _ in range(len(c)):
                    b.append(c.pop())
                c.append(a.pop())
            else:
                for _ in range(len(b)):
                    c.append(b.pop())
                b.append(a.pop())
            return solve(a, b, c)
    return solve(a, b, c)
    
