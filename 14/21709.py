def to_4(num):
    res = ''
    while num > 0:
        res += str(num%4)
        num //= 4
    return res[::-1]

maxx = 0
result = 0

for x in range(1, 3001):
    res = 4**210 + 4**110 - x
    res_4 = to_4(res)
    
    if res_4.count("0") > maxx:
        maxx = res_4.count("0")
        result = x

print(result)