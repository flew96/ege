def del_(n, m):
    return (n%m == 0)

for a in range(1, 10000):
    flag = True
    for x in range(10000):
        if not(
            del_(x, 33) <= ((not del_(x, a)) <= (not del_(x, 242)))
        ):
            flag = False
    
    if flag:
        print(a)