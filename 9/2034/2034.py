f = open(r"9\2034\2034.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    
    return (
        (sum(row) == 180) and
        (0 not in row)
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)