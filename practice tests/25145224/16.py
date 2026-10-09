from sys import setrecursionlimit

def f(n):
    if n < 20:
        return 10
    if n >= 20 and n % 2 == 0:
        return (f(n/2) + n - 3)
    elif n >= 20 and n % 2 == 1:
        return (f(n-2) + 6)

setrecursionlimit(30000)

lst = []
for n in range(-30000, 30000):
    if 100000 <= abs(f(n)) <= 9999999:
        lst.append(n)

print(min(lst))