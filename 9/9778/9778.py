f = open(r"9\9778\9778.txt")

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
        (len(repeatable) == 2) and
        (repeatable[0] >= (sum(uniq) / 4))
    )


count = 0
for row in data:
    count += 1
    if check(row):
        print(count)
        break