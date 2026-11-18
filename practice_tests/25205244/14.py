from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:12]

for x in alph:
    num = (
        int(f"27{x}98966", 22) +
        int(f"26{x}33", 22) +
        int(f"522{x}5", 22)
    )
    
    if num%21 == 0:
        print(num/21)