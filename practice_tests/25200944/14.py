from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:15]

for x in alph:
    num1 = int(f"689{x}245", 25)
    num2 = int(f"486{x}158", 25)

    num = num1 + num2

    if num % 24 == 0:
        print(num / 24)
        break