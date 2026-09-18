f = open(r"practice tests\25203502\9\9.txt")

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
        (sum(repeatable) > sum(uniq))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)