def to_3(n):
    res = ''
    while n > 0:
        res += str(n%3)
        n //= 3
    return res[::-1]

print(to_3(34066))

1201201201

print(int("11201201201", 3))