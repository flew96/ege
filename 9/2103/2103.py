f = open(r"9\2103\2103.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    
    return (
        row[0] == row[2]
        and row[1] == row[3]
        and row[0] != row[1]
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)