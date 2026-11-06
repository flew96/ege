def del_(x, a):
    return (x % a == 0)

for a in range(1, 1500):
    flag = True

    for x in range(1, 1500):
        if not (
            (not del_(x, 84) or not del_(x, 90)) <= (not del_(x, a))
        ):
            flag = False

    if flag:
        print(a)
        break