def to_7(n):
    res = ''
    
    while n > 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]


for x in range(1, 2031):
    res = 7**170 + 7**100 - x
    
    res_7 = to_7(res)
    
    if res_7.count("0") == 70:
        print(x)