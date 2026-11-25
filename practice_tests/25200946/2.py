from itertools import product, permutations

def f(x, y, w, z):
    return (
        (not (y == x)) and (w or y) and z
    )

for a in product([0, 1], repeat=7):
    table = [
        (0, a[0], 0, a[1]),
        (1, a[2], a[3], 1),
        (a[4], a[5], a[6], 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(p)