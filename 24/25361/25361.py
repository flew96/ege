f = open("24/25361/24_25361.txt").read()

for even in "02468":
    f = f.replace(even, "*")

indexes = []


for i in range(len(f)):
    if f[i] == "F":
        indexes.append(i)



def clean(sub: str):
    # 123..AASDASD123F
    left_part = ''
    for i in range(sub.index("F") - 1, -1, -1):
        if sub[i] != "*":
            left_part += sub[i]
        else:
            left_part += sub[i]
            break

    right_part = sub[sub.index("F"):]

    if "*" in right_part or "*" not in left_part:
        return False
    return left_part[::-1] + right_part

max_len = 0

for i in range(len(indexes) - 77):
    left = indexes[i]
    right = indexes[i + 77]

    sub = f[left + 1: right]
    # print(sub.count("F"), sub[:10], sub[-10:])

    sub = clean(sub)

    if sub:
        max_len = max(max_len, len(sub))

print(max_len)