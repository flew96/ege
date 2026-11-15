f = open("24/26077/24_26077.txt").read()

for odd in "13579":
    f = f.replace(odd, "*")

indexes = [-1]

for i in range(len(f)):
    if f[i] == "*":
        indexes.append(i)

indexes.append(len(f))


def clean(sub: str):
    left_part = ''
    for i in range(sub.index("*") - 1, -1, -1):
        if sub[i] != "G":
            left_part += sub[i]
        else:
            left_part += sub[i]
            break

    right_part = sub[sub.index("*"):]
    if "G" in right_part:
        right_part = right_part[:right_part.index("G")]

    if right_part.count("*") != 45 or "G" not in left_part:
        return False
    return left_part[::-1] + right_part

max_len = 0

for i in range(len(indexes) - 46):
    left = indexes[i]
    right = indexes[i + 46]

    sub = f[left + 1: right]

    sub = clean(sub)

    if sub:
        max_len = max(max_len, len(sub))

print(max_len)
