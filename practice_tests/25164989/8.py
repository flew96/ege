from itertools import product 

count = 0
for num in product("0123456", repeat=5):
    num = "".join(num)
    
    if (
        (num.count("0") == 1) and
        (num.count("1") <= 2)
    ):
        count += 1

print(count)