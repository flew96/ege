from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:13]

for x in alph:
    num = (
        int("81" + x + "9982", 23) +
        int("36" + x + "24", 23) +
        int("72" + x + "5", 23)
    )

    if num % 22 == 0:
        print(num // 22)
        break