from itertools import product

def check(num: str):
    for i in "ABC":
        num = num.replace(i, "_")
    
    return num.count("_") == 2 and "__" in num

counter = 0
for num in product("0123456789ABC", repeat=6):
    num = "".join(num)
    
    if (
        num.count("0") >= 2 and
        check(num) and
        num[0] != "0"
    ):
        counter += 1
    
print(counter)