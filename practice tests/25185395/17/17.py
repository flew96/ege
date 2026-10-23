f = open(r"practice tests\25185395\17\17_29349 (1).txt")

data = [int(i) for i in f]

min_pos_123 = (10**6)
for i in data:
    if (i % 123 == 0) and i > 0:
        min_pos_123 = min(i, min_pos_123)

def check(row: list):
    return (
        sum(row) < min_pos_123
    )

count = 0
max_sum = -10**6
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)
        