from itertools import product

index = 1
count = 0

for word in product(sorted("ЦИФЕРБЛАТ"), repeat=5):
    word = "".join(word)
    
    if (
        index % 2 == 1 and
        word[0] not in "ИЕА" and
        word.count("Ц") == word.count("Ф")
    ):
        count += 1
        
    
    index += 1

print(count)