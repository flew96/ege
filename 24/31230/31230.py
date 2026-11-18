f = open(r"24/31230/24_31230 (1).txt").read()

f = f.replace("ABC", "*")

indexes = []
for i in len(f):
    if f[i] == "*":
        indexes.append(i)

for i in range(len(indexes)):
    left = [i]
    right = [i+109]

    sub = f[left:right+1]
    for i in range(right+1, len(f)):
        if f[i] == "C":
            sub