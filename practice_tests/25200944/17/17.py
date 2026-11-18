f = open(r"practice_tests/25200944/17/17 (1).txt")

data = [int(i) for i in f]

max_el_67 = 10**6
for i in data:
    if (abs(i) % 100 == 67):
        max_el_67 = max(i, max_el_67)

def check(row: list):
    flag = any([100 <= abs(i) <= 999 for i in row])

    return (
        flag and
        (row[0]*row[1]*row[2] < max_el_67)
    )

count = 0
max_sum = -10**6
for i in range(len(data)-2):
    row = data[i:i+3]

    if check(row):
        count += 1
        max_sum = max(sum(row), max_sum)

print(count, max_sum)