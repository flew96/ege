f = open(r"17\23563\17_23563.txt")

data = [int(i) for i in f]

lst = []
for i in data:
    if i > 0 and abs(i) % 35 == 0:
        lst.append(i)
min_pos_45 = min(lst)

def check(row: list):
    return (
        (row[1] != row[0]) and
        abs(row[0] - row[1]) % min_pos_45 == 0
    )

count = 0
max_sum = -200000
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)