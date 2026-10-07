from itertools import product

index = 0
count = 0
for word in product(sorted("ГЕРМАНИЯ"), repeat=6):
    word = "".join(word)
    index += 1
    
    if (
        (index % 2 == 0) and
        (word[0] != "Г") and
        (word.count("И") >= 2)
    ):
        count += 1

print(count )