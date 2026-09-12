from itertools import product

index = 1

for word in product(sorted("СОЛНЦЕ"), repeat=6):
    word = "".join(word)
    
    # print(index, word)
    
    if (
        index % 2 == 1 and
        word[0] not in "ЦН" and
        word.count("Ц") == 1 and
        word.count("Н") == 1
    ):
        print(index, word)
    
    index += 1
    
    # if index == 10:
    #     break

