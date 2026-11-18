from itertools import permutations, product

def f(a, b, c, d):
    return (
        (not (a and (not c))) and
        (not ((c <= d) and (d <= c))) and b
    )

for a in product([0, 1], repeat=3):
    table = [
        (0, 0, a[0], 1),
        (0, 1, 0, 1),
        (1, a[1], 0, a[2])
    ]
    
    if len(table) == len(set(table)):
        for p in permutations("abcd"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(p)