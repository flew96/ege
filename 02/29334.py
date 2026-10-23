from itertools import permutations, product

def f(x, y, w, z):
    return (
        ((z <= x) <= (x == y)) or (not w)
    )

for a in product([0, 1], repeat=5):
    table = [
        (a[0], 0, 1, 0),
        (0, a[1], a[2], 0),
        (a[3], 1, 1, a[4])
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(p)