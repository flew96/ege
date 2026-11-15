f = open(r"24/29354/24_29354.txt").read()


f = f.replace("BC", "*")

indexes = []
for i in range(len(f)):
    if f[i] == "*":
        indexes.append(i)

max_len_sub = 0
for i in range(len(indexes)-191):
    left = indexes[i]
    right = indexes[i+191]

    sub = f[left+1:right]
    max_len_sub = max(max_len_sub, len(sub))

print(max_len_sub + 192)