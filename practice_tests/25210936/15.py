for a in range(0, 500):
    flag = True
    
    for x in range(0, 500):
        for y in range(0, 500):
            if not (
                (x > a) or (y > a) or (11*x + 17*y < 360)
            ):
                flag = False
                
    if flag:
        print(a)