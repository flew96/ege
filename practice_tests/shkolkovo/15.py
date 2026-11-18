from itertools import combinations

def p(x):
    return 25 <= x <= 40

def q(x):
    return 11 <= x <= 32

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([25, 40, 11, 32]),
    r=2
)

dlini = set()

for start, stop in vars:
    flag = True
    
    for x in range(20, 45):
        if not (
            (p(x)) <= (((q(x)) and (p(x))) <= a(x, start, stop))
        ):
            flag = False
    
    if flag:
        dlini.add(stop - start)

print(min(dlini))