f = open(r"practice tests/25145224/17/17.txt")

data = [int(i) for i in f]

count_pos_odd = 0
for i in data:
    if i > 0 and i % 2 == 1:
        count_pos_odd += 1

def check(row: list):
    sum_last_digit = 0
    for i in row:
        sum_last_digit += abs(i) % 10

    return (
        (sum_last_digit % 3 == 0) and
        (max(row) + min(row) <= count_pos_odd)
    )

count = 0
min_sum = 10**6
for i in range(len(data) - 2):
    row = data[i:i+3]

    if check(row):
        count += 1
        min_sum = min(min_sum, sum(row))

print(count, abs(min_sum))