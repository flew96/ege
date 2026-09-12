f = open(r"9\31116\31116.txt")

data = [
    [int(i) for i in row.split()] for row in f
]

def check(row: list):
    repeatable = []
    ordered = sorted(row)
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
    
    return (
        (len(repeatable) == 0) and
        (2*(ordered[0] + ordered[4]) > sum(ordered[1:4]))
    )

for row in data:
    if check(row):
        print(sum(row))
        break
    