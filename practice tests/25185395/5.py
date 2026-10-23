for n in range(1, 10000):
    n_2 = bin(n)[2:]
    
    if (n_2.count("1") % 2 == 0):
        n_2 = "10" + n_2[2:] + "0"
    else:
        n_2 = "11" + n_2[2:] + "1"
    
    r = int(n_2, 2)
    
    if r <= 19:
        print(n)