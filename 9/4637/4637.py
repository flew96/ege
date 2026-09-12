f = open(r"9\4637\4637.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (sorted_row[3]**3) >=
        (sorted_row[0] * sorted_row[1] * sorted_row[2] * 2) and
        (sorted_row[0] > 10)
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)