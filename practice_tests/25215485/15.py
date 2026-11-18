from itertools import combinations

def p(x):
    return 20 <= x <= 150

def q(x):
    return 45 <= x <= 180

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([20, 150, 45, 180]),
    r=2
)

lengths = set()

for start, stop in vars:
    flag = True
    for x in range(1000):
        if  (
            (not q(x) <= ((not a(x, start, stop) and p(x)) <= (not q(x))))
        ):
            flag = False

    if flag:
        lengths.add(stop - start)

print(min(lengths))