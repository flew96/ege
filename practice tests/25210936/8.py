from itertools import product 

index = 0
for word in product(sorted("ЦИФЕРБЛАТ"), repeat=5):
    word = "".join(word)
    index += 1
    
    if (
        (index % 2 == 1) and
        (word[0] not in "РТЕ") and
        (word.count("И") >= 2)
    ):
        print(index)
        print(word)