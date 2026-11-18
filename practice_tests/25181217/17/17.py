f = open(r"practice tests/25181217/17/17_28938.txt")

data = [int(i) for i in f]

max_el_23 = -(10**6)
for i in data:
    if abs(i) % 100 == 23:
        max_el_23 = max(max_el_23, i)


def check(row: list):
    count = 0
    for i in row:
        if 100 <= abs(i) <= 999:
            count += 1

    return (
        (count >= 1) and
        ((sum(row) / 3) > 0) and
        ((sum(row) / 3) < max_el_23)
    )

count = 0
max_sum_el = -(10**6)
for i in range(len(data) - 2):
    row = data[i:i+3]

    if check(row):
        count += 1
        max_sum_el = max(sum(row), max_sum_el)

print(count, max_sum_el)