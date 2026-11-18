from itertools import product

index = 0
for word in product(sorted("СОЛНЦЕ"), repeat=6):
    word = "".join(word)
    index += 1
    
    if (
        (index%2 != 0) and
        (word[0] not in "ЦН") and
        (word.count("Ц") == 1) and
        (word.count("Н") == 1)
    ):
        print(index)
    