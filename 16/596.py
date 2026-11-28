from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n <= 3:
        return n
    elif (
        (n > 3) and
        (n % 3 == 0)
    ):
        return (
            n**3 + f(n-1)
        )
    elif (
        (n > 3) and
        (n % 3 == 1)
    ):
        return (
            4 + f(n//3)
        )
    elif (
        (n > 3) and
        (n % 3 == 2)
    ):
        return (
            n**2 + f(n-2)
        )

print(f(100))