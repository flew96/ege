from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n >= 22:
        return (
            f(n-7) + 567
        )
    else:
        return (
            10 * (g(n-6) - 36)
        )

def g(n):
    if n >= 22242:
        return (
            n/33 + 67
        )
    else:
        return (
            g(n+14) - 4
        )

print(f(1024))