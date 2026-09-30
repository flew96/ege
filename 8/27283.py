from itertools import product

index = 0
for word in product(sorted("ПОЛЕНИЦА"), repeat=5):
    word = "".join(word)
    index += 1

    if (
        (index % 2 == 1) and
        (word[0] != "А") and
        (word[4] != "А") and
        (word.count("Л") >= 3)
    ):
        print(index)
        break