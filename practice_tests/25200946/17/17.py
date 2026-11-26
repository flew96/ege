f = open(r"practice_tests/25200946/17/17 (2).txt")

data = [int(i) for i in f]

min_pos_el_52 = 10**6
for i in data:
    if (
        (i % 52 == 0) and
        (i > 0)
    ):
        min_pos_el_52 = min(min_pos_el_52, i)

def check(row: list):
    return (
        sum(row) < min_pos_el_52
    )


count = 0
max_sum = -10**6
for i in range(len(data) - 1):
    row = data[i:i+2]
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)