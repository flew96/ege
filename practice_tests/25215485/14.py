num = (
    729**12 - 243**3 * 81**10 + 81**6 - 350
)

count = 0
while num > 0:
    if (num%9) == 0:
        count += 1
    num //= 9

print(count)