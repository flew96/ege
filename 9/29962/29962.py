f = open(r"9\29962\29962.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    uniq = []
    repeatable = []
    
    for i in row:
        if row.count(i) == 1:
            uniq.append(i)
        elif row.count(i) == 3:
            repeatable.append(i)
    
    return (
        (len(uniq) == 4) and
        (len(repeatable) == 3) and
        (sum(uniq) / 4 > repeatable[0])
    )

index = 0
for row in data:
    index += 1
    if check(row):
        print(index)