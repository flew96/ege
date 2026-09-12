f = open(r"17\28762\17_28762.txt")

data = [int(i) for i in f]

min_el_23 = 10**6
for i in data:
    if i % 23 == 0:
        min_el_23 = min(min_el_23, i)

def check(row: list):
    for i in row:
        if i % min_el_23 == 0:
            return True
    return False

count = 0
max_sum_el = 0
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)