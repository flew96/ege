f = open(r"17\31124\17_31124.txt")

data = [int(i) for i in f]

lst = []
for i in data:
    if i % 33 == 0 and i > 0:
        lst.append(i)
min_pos_33 = min(lst)


def check(row: list):
    return (
        (row[0] != row[1]) and
        (abs(row[0] - row[1]) % min_pos_33 == 0)
    )


count = 0
max_sum = -9999999999
for i in range(len(data) - 1):
    row = data[i:i+2]
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))
        
print(count, max_sum)