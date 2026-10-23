from itertools import product, permutations 

def f(x, y, z, w):
    return (
        (w == z) or (not (y <= w)) or (not x)
    )
    
for a in product([0, 1], repeat=5):
    table = [
        (0, 0, 1, a[0]),
        (a[1], 1, 1, a[2]),
        (0, a[3], a[4], 0)
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(p)