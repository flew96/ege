def mult(a):
    lst = [int(i) for i in str(a)]
    res = 1
    for i in lst:
        if i != 0:
            res *= i
    
    return res

for a in range(100000, 1000000):
    s = sum([int(i) for i in str(a)])
    m = max([int(i) for i in str(a)])
    n = min([int(i) for i in str(a)])
    p = mult(a)
    b_1 = s - m - n
    b_2 = p - 2*s
    if b_1 > b_2:
        r = str(b_1) + str(b_2)
    else:
        r = str(b_2) + str(b_1)
    
    if r == "26714":
        print(a)