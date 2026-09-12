f = open(r"17\21712\17_21712.txt")

data = [int(i) for i in f]

min_pos_el = 10**6
for i in data:
    if i > 0 and 1000 <= i <= 9999 and i % 10 == 6:
        min_pos_el = min(min_pos_el, i)


def check(row: list):
    count = 0
    for i in row:
        if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 6:
            count += 1
    
    return (
        (count == 1) and
        (sum(row) <= min_pos_el)
    )

count = 0
max_sum_el = -10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)