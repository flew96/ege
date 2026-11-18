from itertools import product, permutations

def f(x, y, w, z):
    return (
        (y and (not x)) or (x == w) or (not z)
    )

for a in product([0, 1], repeat=4):
    table = [
        (a[0], a[1], 0, 0),
        (1, 0, a[2], 0),
        (1, 0, 1, a[3])
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(p)