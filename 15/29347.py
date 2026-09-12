from itertools import combinations

def b(x):
    return 22 <= x <= 40

def c(x):
    return 32 <= x <= 50

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([22, 40, 32, 50]),
    r=2
)

dlini = set()

for start, stop in vars:
    flag = True
    
    for x in range(20, 55):
        if not (
            (not a(x, start, stop)) <=
            ((b(x)) == (c(x)))
        ):
            flag = False
    
    if flag:
        dlini.add(stop - start)

print(min(dlini))