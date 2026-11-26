from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n >= 24:
        return (
            f(n-6) + 2026
        )
    elif n < 24:
        return (
            8*(g(n-5) - 31)
        )

def g(n):
    if n >= 19870:
        return (
            (n/17) + 45
        )
    elif n < 19870:
        return (
            g(n+9) - 6
        )

print(f(684))