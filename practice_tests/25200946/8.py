from itertools import product

num = 0
for word in product(sorted("ПРОГРАММА"), repeat=5):
    word = "".join(word)
    num += 1

    if (
        (num % 2 == 1) and
        (word[0] != "Р") and
        (word[-1] != "Р") and
        (word.count("О") >= 2)
    ):
        print(num)
    