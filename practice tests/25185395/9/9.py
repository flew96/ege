f = open(r"practice tests\25185395\9\9.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (max(row) < sum(sorted_row[:3])) and
        ((min(row) + max(row)) != (sorted_row[1] + sorted_row[2]))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)