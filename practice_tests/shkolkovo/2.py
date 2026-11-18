from itertools import product, permutations

def f(x, y, w, z):
    return (
        ((x <= (not y)) and (x or w)) <= (not z)
    )

for a in product([0, 1], repeat=8):
    table = [
        (a[0], 0, a[1], 0),
        (1, a[2], a[3], a[4]),
        (0, 0, a[5], a[6]),
        (1, 0, a[7], 1)
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0, 0]:
                print(p)