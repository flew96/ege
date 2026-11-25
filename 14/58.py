n = 64**30 + 2**300 -4 

count = 0
while n > 0:
    if n % 8 == 7:
        count += 1
    n //= 8

print(count)