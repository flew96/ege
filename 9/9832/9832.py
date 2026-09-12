f = open(r"9\9832\9832.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    uniq = []
    repeatable = []
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
        else:
            uniq.append(i)
    
    return (
        (len(set(repeatable)) == 2) and
        (len(repeatable) == 4) and
        (max(row) in uniq)
    )

for row in data:
    if check(row):
        print(sum(row))
        break