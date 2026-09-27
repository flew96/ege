f = open(r"9/31506/31506.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)

    return (
        (len(row) == len(set(row))) and
        ((max(row) + min(row))*2 > sum(sorted_row[1:4]))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)