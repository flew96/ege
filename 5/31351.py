for n in range(1, 10000):
    two_n = bin(n)[2:]
    
    summ = two_n.count("1")
    if summ % 2 == 0:
        two_n = two_n[2:]
        two_n = "10" + two_n + "0"
    else:
        two_n = two_n[2:]
        two_n = "11" + two_n + "1"
    
    r = int(two_n, 2)
    
    if r >= 16:
        print(n)
        break