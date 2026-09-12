f = open(r"17\31225\17_31225.txt")

data = [int(i) for i in f]

max_el = -10**6
for i in data:
    if abs(i) % 10 == 9 and 1000 <= abs(i) <= 9999:
        max_el = max(max_el, i)


def check(row: list):
    count = 0
    
    for i in row:
        if abs(i) % 10 == 9 and 1000 <= abs(i) <= 9999:
            count += 1
    
    return (
        (count == 2) and
        (sum(row) < max_el)
    )

count = 0
max_sum = -10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)
        