from itertools import product

index = 0
for word in product(sorted("ЭКРАН"), repeat=6):
    word = "".join(word)
    index += 1

    if (
        (word[0] != "А") and
        (word.count("К") <= 1) and
        ("ЭЭ" not in word)
    ):
        print(index)
        break