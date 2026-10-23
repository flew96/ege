lst = []
for n in range(1, 10000):
    n_2 = bin(n)[2:]
    
    if n % 2 == 0:
        n_2 = "11" + n_2 + "11"
    else:
        n_2 = "1" + n_2 + "00"
    
    r = int(n_2, 2)
    
    if r > 95:
        lst.append(r)

print(min(lst))