for a in range(300):
    flag = True
    
    for x in range(300):
        for y in range(300):
            if not (
                (x + y <= 27) or (y <= x -1) or (y >= a)
            ):
                flag = False
    
    if flag:
        print(a)