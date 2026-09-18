from sys import setrecursionlimit
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n-1) * f(n-1)

setrecursionlimit(35000)

print(
    (3*f(32028) - f(32027))/f(32026)
)