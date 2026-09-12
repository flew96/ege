from string import ascii_uppercase, digits

alph = digits + ascii_uppercase[:12]

for x in alph:
    res = (int(f"27{x}98966", 22) + 
           int(f"26{x}33", 22) + 
           int(f"522{x}5", 22))
    
    if res % 21 == 0:
        print(x, res // 21)

