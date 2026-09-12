f = open(r"17\23201\17_23201.txt")

data = [int(i) for i in f]

min_el_7 = 10**6
for i in data:
    if 100 <= abs(i) <= 999 and abs(i) % 10 == 7:
        min_el_7 = min(min_el_7, i)

def check(row: list):
    count = 0
    for i in row:
        if 100 <= abs(i) <= 999:
            count += 1

    return (
        (count == 1) and
        (sum(row) % min_el_7 == 0)
    )

count = 0
min_sum_el = 10**6
for i in range(len(data) - 1):
    row = data[i:i+2]

    if check(row):
        count += 1
        min_sum_el = min(min_sum_el, sum(row))

print(count, min_sum_el)