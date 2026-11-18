from itertools import combinations

def a(x, start, stop):
    return start <= x <= stop

def b(x):
    return 19 <= x <= 28

def c(x):
    return 25 <= x <= 42

vars = combinations(
    sorted([19, 28, 25, 42]),
    r=2
)

lengths = set()

for start, stop in vars:
    flag = True

    for x in range(15, 45):
        if not(
            (not (b(x) == c(x))) <= (a(x, start, stop) or (a(x, start, stop) and b(x)))
        ):
            flag = False

    if flag:
        lengths.add(stop-start)

print(min(lengths))