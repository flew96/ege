f = open(r"9\9740\9740.txt")

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
        (len(repeatable) == 3) and
        ((sum(uniq) / 4) <= repeatable[0])
    )


count = 0
for row in data:
    if check(row):
        count += 1

print(count)