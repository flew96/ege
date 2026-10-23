from itertools import product

index = 0
for word in product(sorted("ПЛАНЕР"), repeat=6):
    word = "".join(word)
    index += 1
    
    if (
        (index % 2 == 1) and
        ("П" not in word) and
        ("Р" not in word) and
        (word.count("А") == 2) and
        (word.count("Н") == 1)
    ):
        print(index)