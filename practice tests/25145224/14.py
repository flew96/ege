from string import ascii_uppercase, digits

alph_21 = digits + ascii_uppercase[:11]

for x in alph_21:
    num = (
        int(f"4B3{x}1C7", 21) +
        int(f"I6HA2K", 22) +
        int(f"5{x}G83F7", 23)
    )

    if num % 66 == 0:
        print(num/66)