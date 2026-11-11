f = open(r"24/26077/24_26077.txt").read()

for i in "13579":
    f = f.replace(i, "*")


indexes = [-1]
for i in range(len(f)):
    if f[i] == "*":
        indexes.append(i)
indexes.append(len(f))

def clean_g(s: str):
    p = -1
    for i in range(s.index("*")):
        if s[i] == "G":
            p = i
    if p == -1:
        return ""
    s = s[p:]
    if s.count("G") > 1:
        s = s[:s.index("G", 1)]
    return s


max_len = 0
for i in range(len(indexes)-46):
    left = indexes[i]
    right = indexes[i+46]

    sub_s = clean_g(f[left+1:right])
    if sub_s.count("*") == 45:
        max_len = max(len(sub_s), max_len)

print(max_len)
