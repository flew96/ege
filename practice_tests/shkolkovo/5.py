for n in range(1, 10000):
    n_2 = bin(n)[2:]
    
    if (n%2 == 1):
        n_2 = "0" + n_2 + "1"
    else:
        n_2 = n_2 + bin(n_2.count("1"))[2:]
    
    r = int(n_2, 2)
    if r == 603:
        print(n)
