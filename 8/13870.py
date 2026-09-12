from itertools import product


def check(num: str):
    for i in "01234567":
        if (
            i*3 in num and
            num.count(i) == 3 and
            len(set(num)) == len(num) - 2
        ):
            return True
    return False

lst = []

for num in product("01234567", repeat=5):
    num = "".join(num)
    
    if check(num) and num[0] != "0":
        lst.append(num)

print(len(lst))