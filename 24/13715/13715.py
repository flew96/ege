f = open(r"24/13715/24_13715.txt").read()



indexes = []
sub_s = ''

skip_next = False

for i in range(1, len(f)-1):
    if skip_next:
        skip_next = False
        continue
    if (f[i] == "A" and f[i-1] == "B") or (f[i] == "B" and f[i-1] == "A"):
        indexes.append(i)
        skip_next = True

max_len_sub = 0
for i in range(len(indexes)-51):
    left = indexes[i]
    right = indexes[i+51]

    sub_s = f[left:right+2]
    max_len_sub = max(max_len_sub, len(sub_s)-2)
    # print(sub_s, end="\n")

print(max_len_sub)