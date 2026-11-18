for a in range(300):
    flag = True
    for y in range(300):
        for x in range(300):
            if not (
                (x > 67) or
                (y >= x) or
                (3*x - y < a)
            ):
                flag = False
    
    if flag:
        print(a)
        break