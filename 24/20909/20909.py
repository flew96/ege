f = open(r"24\20909\24_20909.txt").read()

f = f.replace("AB", "&")

indexes = []

for i in range(len(f)):
    if f[i] == "&":
        indexes.append(i)

max_len_sub = 0
for i in range(len(indexes)-101):
    left = indexes[i]
    right = indexes[i + 101]
    
    sub = f[left+1:right]
    
    max_len_sub = max(len(sub), max_len_sub)

print(max_len_sub + 102)