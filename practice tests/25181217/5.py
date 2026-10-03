def to_3(n):
    res = ''
    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]


lst = []
for n in range(1, 10000):
    n3 = to_3(n)

    if n % 3 == 0:
        n3 = n3 + n3[-2:]
    else:
        n3 = n3 + to_3(sum(int(i) for i in n3)*2) 

    r = int(n3, 3)
    if (r % 2 == 1) and (r > 520):
        lst.append(r)

print(min(lst))