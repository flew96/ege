f = open(r"9\4636\4636.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (sorted_row[3] - sorted_row[0] >= 50) and
        (sorted_row[1] * sorted_row[2] <= 1000)
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)