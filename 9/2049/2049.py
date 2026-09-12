f = open(r"9\2049\2049.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (sorted_row[0] != sorted_row[1]) and
        (sorted_row[2] - sorted_row[1] == sorted_row[1] - sorted_row[0])
    )


count = 0
for row in data:
    if check(row):
        count += 1
print(count)