f = open(r"practice tests\25203502\17\17_31225 (1).txt")

data = [int(i) for i in f]

max_el_9 = -10**6
for i in data:
    if abs(i) % 10 == 9 and 1000 <= abs(i) <= 9999:
        max_el_9 = max(max_el_9, i)


def check(row: list):
    count = 0
    for i in row:
        if abs(i) % 10 == 9 and 1000 <= abs(i) <= 9999:
            count += 1
    
    return (
        (count == 2) and
        (sum(row) < max_el_9)
    )

count = 0
max_sum = -10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum = max(sum(row), max_sum)

print(count, max_sum)