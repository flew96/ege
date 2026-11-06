from itertools import combinations

def p(x):
    return 17 <= x <= 54

def q(x):
    return 37 <= x <= 83

def a(x, start, stop):
    return start <= x <= stop


vars = combinations(
    sorted([17, 54, 37, 83]),
    r=2
)

lengths = set()

for start, stop in vars:
    flag = True
    for x in range(15, 85):
        if not (
            p(x) <= (((q(x) and (not a(x, start, stop))) <= (not p(x))))
        ):
            flag = False

    if flag:
        lengths.add(stop - start)

print(min(lengths))