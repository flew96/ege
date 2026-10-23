f = open(r"09/03167/03167.txt")

data = [
    [int(i) for i in row.split()] for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (min(row) + max(row))**2 > (sorted_row[1]**2 + sorted_row[2]**2)
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)