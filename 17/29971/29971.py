f = open(r"17\29971\17_29971.txt")

data = [int(i) for i in f]

max_el_33 = -10**6
for i in data:
    if abs(i) % 100 == 33:
        max_el_33 = max(max_el_33, i)

def check(row: list):
    count = 0
    for i in row:
        if 10 <= abs(i) <= 99:
            count += 1
    
    return (
        (count == 2) and
        (sum(row)** 2 < max_el_33)
    )

count = 0
max_sum_el = 0
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)