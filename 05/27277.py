def to_3(num):
    res = ''
    while num > 0:
        res += str(num%3)
        num //= 3
    return res[::-1]


for n in range(1, 10000):
    n_3 = to_3(n)
    if n % 3 != 0:
        n_3 = "1" + n_3 + n_3[-3:]
    else:
        sum_dig = sum([int(i) for i in n_3])
        n_3 = n_3 + to_3(sum_dig*8)
    
    r = int(n_3, 3)
    if 1150 < r < 1290:
        print(r)