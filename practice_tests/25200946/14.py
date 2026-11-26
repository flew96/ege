from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:11]

for x in alph:
    num = (
        int(f"197{x}627", 21) + int(f"634{x}542", 21)
    )

    if num % 20 == 0:
        print(num / 10)

#answ = 65173860