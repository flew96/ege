from itertools import permutations, product

def f(w, x, y, z):
    return (not (z <= x)) or (y <= w) or (not y)

for a in product([0, 1], repeat=7):
    table = [
        (0, 1, a[0], a[1]),
        (a[2], 0, a[3], a[4]),
        (1, a[5], 0, a[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(p)