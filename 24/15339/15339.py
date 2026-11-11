f = open(r"24/15339/24_15339.txt").read()

f = f.replace("B", "A")
f = f.replace("C", "A")
f = f.replace("7", "6")
f = f.replace("8", "6")
f = f.replace("9", "6")


res = []

temp_s = f[0]

for i in range(1, len(f)):
    if f[i] != temp_s[-1]:
        temp_s += f[i]
    else:
        res.append(len(temp_s))
        temp_s = f[i]

res.append(len(temp_s))

print(max(res))
