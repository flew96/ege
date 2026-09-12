from string import ascii_uppercase, digits


res = (5*1296**2021 -
       4*216**2022 +
       3*36**2023 -
       2*6**2024 - 
       2025)

alph = digits + ascii_uppercase

def to_36(num):
    res = ''
    
    while num > 0:
        res += alph[num%36]
        num //= 36
    
    return res[::-1]

res_36 = to_36(res)

count = 0
for i in res_36:
    if int(i, 36) % 2 == 0:
        count += 1
        
print(count) 