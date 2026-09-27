from itertools import product

index = 0
for word in product(sorted("АПРЕЛЬ"), repeat=5):
    word = "".join(word)
    index += 1

    if (
        (index % 2 == 0) and
        (word[0] not in "ЬР") and
        (word.count("Л") >= 2)
    ):
        print(index)