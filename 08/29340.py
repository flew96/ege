from itertools import product

index = 0
for word in product(sorted("АПРЕЛЬ"), repeat=6):
    word = "".join(word)
    index += 1
    
    if (
        (index % 2 == 1) and
        (word[0] not in "АЛ") and
        (word.count("П") >= 2)
    ):
        print(index)
        break