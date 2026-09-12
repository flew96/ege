from sys import setrecursionlimit

setrecursionlimit(30000)

def f(n):
    if n < 17:
        return 6
    return (n + 5) * f(n - 9)

print(
    (f(234561) // 436 + f(234552) // 218) // f(234534)
)