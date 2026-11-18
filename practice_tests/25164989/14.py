from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:12]

maxx = 0
for x in alph:
    num = (
        int(f"12313{x}57", 22) +
        int(f"1{x}34561", 22)
    )
    
    if num % 21 == 0:
        maxx = max(maxx, (num / 21))

print(maxx)