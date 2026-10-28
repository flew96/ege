f = open(r"practice tests\25210936\9\9.txt")

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
        (len(set(repeatable)) == 1) and
        (max(row)**3 > uniq[0]*uniq[1]*uniq[2])
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)