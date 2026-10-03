
for a in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not (
                (x * y < a) or
                (5 * x < y) or
                (486 <= x)
            ):
                flag = False

    if flag:
        print(a)
        break