f = open(r"9\31147\31147.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    repeatable = []
    lst = sorted(row)
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
    
    return (
        (len(repeatable) == 0) and
        (sum(lst[:3])*2 < sum(lst[3:]))
    )

count = 0
for row in data:
    count += 1
    if check(row):
        print(count)