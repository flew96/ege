for n in range(1, 10000):
    n2 = bin(n)[2:]

    if (n%4 == 0):
        n2 = n2[-3:] + n2
    else:
        n2 = n2 + bin((n%4)*3)[2:]

    r = int(n2, 2)

    if r >= 328:
        print(n)
        break