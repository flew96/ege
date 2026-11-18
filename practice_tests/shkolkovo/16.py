from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n >= 10000:
        return 1
    if n < 10000 and n%2==0:
        return 2*n + f(n+1)
    else:
        return f(n+2) + n
    

print(f(2022) - f(2025))