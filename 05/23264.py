def to_3(n):
    res = ''
    
    while n > 0:
        res += str(n%3)
        n //= 3
    return res[::-1]

lst = []

for n in range(1, 10000):
    three_n = to_3(n)
    
    if n % 3 == 0:
        three_n = three_n + three_n[-2:]
    else:
        three_n = three_n + to_3((n % 3) * 5)
    
    r = int(three_n, 3)
    if r > 150:
        lst.append(r)
    
print(min(lst))
    
