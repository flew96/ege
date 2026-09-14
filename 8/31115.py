from itertools import product 

index = 0
for word in product(sorted("АКЦЕНТ"), repeat=5):
    word = "".join(word)
    index += 1
    
    if (
        (index%2 == 0) and
        (word[0] not in "АЕК") and
        (word.count("Ц") >= 2)
    ):
        print(index)
        break