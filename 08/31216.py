from itertools import product

index = 1
lst = []

for word in product(sorted("ЦВЕТОК"), repeat=6):
    word = "".join(word)
    
    if (
        index % 2 == 1 and
        "Е" not in word and
        "К" not in word and
        word.count("Т") == 2 and
        word.count("Ц") == 1
    ):
        print(index, word)
        lst.append(word)
        
    
    # print(index, word)
    index += 1

print(len(lst))