def f(n):
    if n <= 3:
        return 3
    elif (n > 3 and n % 2 == 0):
        return (
            f(n//2) + 5
        )
    elif (n > 3 and n % 2 == 1):
        return (
            f(n-1) - f(n-2)
        )

print(f(20))