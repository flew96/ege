from itertools import permutations, product

def f(x, y, z, w):
    return (
        (x <= y) and z and (not w)
    )


for a in product([0, 1], repeat=6):
    table = [
        (0, 1, a[0], a[1]),
        (1, 1, a[2], a[3]),
        (1, a[4], 1, a[5])
    ]

    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(p)