f = open(r"9\3150\3150.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (sorted_row[2]**2 > (sorted_row[0]*sorted_row[1]*2))
    )

count = 0
for row in data:
    if check(row):
        count += 1
print(count)