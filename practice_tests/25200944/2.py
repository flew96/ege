from itertools import product, permutations

def f(x, y, w, z):
    return (
        (not (z == w)) and (not y) and (x or z)
    )

for a in product([0, 1], repeat=7):
    table = [
        (1, a[0], a[1], a[2]),
        (a[3], 1, 1, a[4]),
        (1, 1, a[5], a[6])
    ]

    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(p)