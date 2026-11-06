from itertools import combinations

def b(x):
    return 18 <= x <= 52

def c(x):
    return 16 <= x <= 41

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([18, 52, 16, 41]),
    r=2
)

print(*vars)

lenghts = set()

for start, stop in vars:
    flag = True
    for x in range(14, 55):
        if not (
            (b(x) <= a(x, start, stop) and ((not c(x)) or a(x, start, stop)))
        ):
            flag = False

    if flag:
        lenghts.add(stop - start)

print(min(lenghts))