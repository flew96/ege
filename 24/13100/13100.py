f = open(r"24\13100\24_13100.txt").read()

indexes = []

for i in range(len(f)):
    if f[i] == "C" or f[i] == "D":
        indexes.append(i)
        
max_sub_len = 0
for i in range(len(indexes)-5):
    left = indexes[i]
    right = indexes[i+5]
    
    sub = f[left+1:right]
    
    if sub.count("C") == sub.count("D"):
        max_sub_len = max(max_sub_len, len(sub))

print(max_sub_len)  