f = open(r"practice tests/25181217/9/9.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)

    return (
        (sorted_row == row) and
        ((min(row) + max(row)) <= sum(sorted_row[1:5]))
    )

count = 0
for row in data:
    if check(row):
        count +=1

print(count)