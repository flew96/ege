from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n >= 10**4:
        return n
    else:
        return (
            f(n+4) * (n-4)
        )

print(
    (f(2012)//8 - 121*f(2016))/f(2020)
)
