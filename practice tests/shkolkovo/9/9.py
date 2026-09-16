f = open(r"practice tests\shkolkovo\9\9.txt")

data = [[int(i) for i in row.split()]for row in f
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
        ((sum(uniq) / 4) <= repeatable[0]) and
        (max(row) % min(row) != 0)
    )

max_sum = -10**6
index = 0
for row in data:
    index += 1
    if check(row) and sum(row) == 1724:
        print(index)
        

print(index)