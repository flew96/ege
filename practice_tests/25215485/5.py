min_r = 10**6

for n in range(2, 10000, 2):
    n2 = bin(n)[2:]

    if (n % 3 == 0):
        n2 = "1" + n2[:-2] + "11"
    else:
        n2 = "10" + n2 + "0"

    r = int(n2, 2)

    if r > 2000:
        min_r = min(r, min_r)
        print(r)

print(min_r)