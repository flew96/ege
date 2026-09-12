f = open(r"9\31217\31217.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    uniq = []
    repeatable = []
    
    for i in row:
        if row.count(i) == 2:
            repeatable.append(i)
        elif row.count(i) == 1:
            uniq.append(i)
    
    return (
        (len(repeatable) == 4) and 
        (len(set(repeatable)) == 2) and
        (sum(repeatable) > sum(uniq))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)