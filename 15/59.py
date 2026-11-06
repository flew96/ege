def del_(n, m):
    return (n % m == 0)

for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        if not (
            (del_(x, a) and del_(x, 24) and (not del_(x, 16))) <= (not del_(x, a))
        ):
            flag = False

    if flag:
        print(a)
        break