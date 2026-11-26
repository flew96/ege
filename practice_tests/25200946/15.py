from itertools import combinations

def p(x):
    return 21 <= x <= 47

def q(x):
    return 39 <= x <= 64

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([21, 47, 39, 64]),
    r=2
)

lengths = set()

for start, stop in vars:
    flag = True
    for x in range(1, 1000):
        if not (
            p(x) <= ((q(x) and ((not q(x)) or (not a(x, start, stop)))) <= (not p(x)))
        ):
            flag = False
            break

    if flag:
        lengths.add(stop - start)

print(min(lengths))

#answ = 8