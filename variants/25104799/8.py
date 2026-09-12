from itertools import product

for index, word in enumerate(
    list(product(sorted("АЛГОРИТМ"), repeat=5)), start=1):
    
    word = "".join(word)
    
    if (
        (index % 2 == 0) and
        (word[0] != "Т" and word[0] != "Р") and
        (word.count("И") >= 2)
    ):
        print(index, word)