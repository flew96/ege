from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:13]

for x in alph:
    num = (
        int(f"761{x}035", 23) +
        int(f"338{x}932", 23)
    )

    if num % 22 == 0:
        print(num / 22)