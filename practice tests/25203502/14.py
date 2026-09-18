from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:9]

for x in alph:
    num = (
        int(f"76{x}79645", 19) +
        int(f"35{x}42", 19) +
        int(f"332{x}6", 19)
    )
    
    if num % 18 == 0:
        print(num / 18)