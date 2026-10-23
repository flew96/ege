from itertools import product

index = 0
for word in product(sorted('СИМВОЛ'), repeat=5):
    word = "".join(word)
    index += 1

    if (
        (index % 2 == 1) and
        (word[0] not in "ОС") and
        (word.count("В") == 1) and
        (word.count("С") <= 1)
    ):
        print(index)