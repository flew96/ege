f = open(r"09/04614/04614.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    repeatable = []
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
    
    return (
        (sorted_row[3] < sum(sorted_row[:3])) and
        (len(repeatable) == 2)
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)