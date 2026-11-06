def del_(n, m):
    return (n % m == 0)

for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        if not (
            (del_(x, 15) and (not del_(x, 21))) <= ((not del_(x, a)) or (not del_(x, 15)))
        ):
            flag = False

    if flag:
        print(a)
        break