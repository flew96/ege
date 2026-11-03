f = open(r"practice tests/25215485/9.py/9.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)

    return (
        (len(row) == len(set(row))) and
        ((max(row) + min(row))**2 > sorted_row[1]**3 + sorted_row[2]**3)
    )
num = 0
sum_of_nums = 0
for row in data:
    num += 1
    if check(row):
        sum_of_nums += num

print(sum_of_nums)