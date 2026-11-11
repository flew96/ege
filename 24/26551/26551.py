from string import digits, ascii_uppercase

f = open(r"24/26551/24_26551.txt").read()

alph = digits + ascii_uppercase[:4]

def clean_num(num: str):
    while num and (int(num[-1], 14) % 2 != 0):
        num = num[:-1]

    return num

s = ''
res = []
lenghts = []
for i in f:
    if i in alph:
        s += i
    else:
        res.append(s)
        s = ''

res = [i.lstrip("0") for i in res if len(i)]

for i in res:
    lenghts.append(len(clean_num(i)))

print(max(lenghts))