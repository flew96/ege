f = open(r"24/25361/24_25361.txt").read()

for i in '02468':
    f = f.replace(i, "*")

def clean_even(s: str):
    p = -1
    for i in range(s.index("F")):
        if s[i] == "*":
            p = i
    if p == -1:
        return ""
    s = s[p:]
    if s.count("*") > 1:
        s = s[:s.index("*", 1)]
    return s

indexes = [-1]
for i in range(len(f)):
    if f[i] == "F":
        indexes.append(i)
indexes.append(len(f))


max_len = 0
for i in range(len(indexes)-77):
    left = indexes[i]
    right = indexes[i+77]


    sub_s = clean_even(f[left+1:right])
    if sub_s.count("F") == 76:
        max_len = max(len(sub_s), max_len)


    

print(max_len)