from itertools import product

index = 0 
for word in product(sorted("СЛЕПОК"), repeat=6):
    word = "".join(word)
    index += 1

    if (
        (index % 2 == 1) and
        (word[0] not in "СЛ") and
        (word.count("С") == 1) and
        (word.count("Е") == 1)
    ):
        print(index)
        print(word)