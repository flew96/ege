from itertools import product

index = 0
count = 0

for word in product(sorted("ЦВЕТОК"), repeat=6):
    word = "".join(word)
    index += 1
    
    if (
        (index % 2 == 1) and
        ("В" not in word) and
        ("Е" not in word) and
        ("К" not in word) and
        (word.count("Т") == 2) and
        (word.count("Ц") == 1)
    ):
        count += 1

print(count)