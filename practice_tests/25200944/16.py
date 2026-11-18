from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    return (
        4*g(n-5) + 3
    )

def g(n):
    if n <= 16:
        return (
            2*n - 7
        )
    return (g(n-4) + 3)

print(f(42567))