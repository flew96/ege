from itertools import product

def check(num: str):
    count = 0
    for i in "ABCDE":
        count += num.count(i)
    return count >= 2

count = 0

for num in product("0123456789ABCDE", repeat=5):
    num = "".join(num)
    
    if (
        num[0] != "0" and
        num.count("8") == 1 and
        check(num)
    ):
        count += 1

print(count)