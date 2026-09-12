def to_4(n):
    res = ''
    
    while n > 0:
        res += str(n%4)
        n //= 4
    
    return res[::-1]

result = []

for n in range(1, 10000):
    four_n = to_4(n)
    if four_n[0] == "3":
        four_n = four_n.replace("1", "!")
        four_n = four_n.replace("3", "1")
        four_n = four_n.replace("!", "3")
        four_n = "21" + four_n
    else:
        four_n = "1" + four_n[1:] + "12"
        
    r = int(four_n, 4)
    if r == 597:
        print(n)