from string import ascii_uppercase, digits

alph = digits + ascii_uppercase

def to_36(n):
    res = ''
    while n > 0:
        res += alph[n%36]
        n //= 36
    return res[::-1]

num = to_36(
    5* 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025
)

count = 0
for i in num:
    if int(i, 36) % 2 == 0:
        count += 1

print(count)