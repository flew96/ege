def del_(n, m):
    return n % m == 0

for a in range(1, 300):
    flag = True
    
    for x in range(1, 300):
        if not (
            del_(x, a) or 
            ((x in range(70,91)) <= (not del_(x, 16)))
        ):
            flag = False
    
    if flag:
        print(a)