from itertools import product

count = 0
for num in product("0123456", repeat=5):
    num = "".join(num)
    
    if (
        (num[0] in "246") and
        (num[4] not in "23") and
        (num.count("1") >= 2)
    ):
        count += 1

print(count)