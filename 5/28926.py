def to_3(n):
    res = ''
    
    while n > 0:
        res += str(n%3)
        n //= 3
    
    return res[::-1]

result = []

for n in range(1, 100000):
    three_n = to_3(n)
    
    if n % 3 == 0:
        three_n += three_n[-2:]
    else:
        summ = three_n.count("1") + 2 * three_n.count("2")
        summ *= 2
        summ = to_3(summ)
        three_n += summ
    
    r = int(three_n, 3)
    if r > 520 and r % 2 == 1:
        result.append(r)

print(min(result))