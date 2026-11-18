from string import ascii_uppercase, digits

alph = digits + ascii_uppercase[:20]

for x in alph:
    
    expr = (int(f"7{x}A9F", 30) + 
            int(f"1B3{x}", 30))
    
    if expr % 29 == 0:
        print(expr / 29)
        break