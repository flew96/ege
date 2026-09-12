f = open(r"17\23757\17_23757.txt")

data = [int(i) for i in f]

min_2_dig = 10**6
for i in data:
    if 10 <= abs(i) <= 99:
        min_2_dig = min(min_2_dig, i)

def check(row: list):
    count = 0
    
    for i in row:
        if 10 <= abs(i) <= 99:
            count += 1
    
    return (
        (count == 1) and
        (sum(row) % min_2_dig == 0)
    )

count = 0
max_sum_el = 0
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)