f = open(r"17_31155.txt")

data = [int(i) for i in f]

count_100 = 0
for i in data:
    if abs(i) % 100 == 0:
        count_100 += 1


def check(row: list):
    return (
        (row[0] < 0 or row[1] < 0) and
        (sum(row) < count_100)
    )



count = 0
max_sum = -99999999999
for i in range(len(data) - 1):
    row = data[i:i+2]
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)