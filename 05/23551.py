lst = []

for n in range(1, 10000):
    two_n = bin(n)[2:]
    
    if n % 2 == 0:
        two_n = two_n + "10"
    else:
        two_n = "1" + two_n + "01"
    
    r = int(two_n, 2)
    if r < 30:
        lst.append(n)
        
print(max(lst))