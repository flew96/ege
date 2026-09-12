def to_3(n):
    res = ''
    while n > 0:
        res += str(n%3)
        n //= 3
    
    return res[::-1]

for n in range(30000):
    n_3 = to_3(n)
    
    if n%3 == 0:
        n_3 = "1" + n_3 + "02"
    else:
        n_3 = n_3 + to_3((n%3)*4)
    
    r = int(n_3, 3)
    if r < 199:
        print(n)