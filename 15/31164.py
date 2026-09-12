from itertools import combinations

def b(x):
    return 32 <= x <= 425

def c(x):
    return 130 <= x <= 480

def d(x):
    return 290 <= x <= 575

def a(x, start, stop):
    return start <= x <= stop

vars = combinations(
    sorted([32, 425, 130, 480, 290, 575]),
    r=2
)

dlini = set()

for start, stop in vars:
    flag = True
    
    for x in range(30, 580):
        if  (
            (c(x) <= (not d(x))) and 
            a(x, start, stop) and 
            (not b(x))
        ):
            flag = False
    
    if flag:
        dlini.add(stop - start)

print(max(dlini))