f = open(r"9\31355\31355.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    povtor = []
    uniq = []
    
    for i in row:
        if row.count(i) == 3:
            povtor.append(i)
        elif row.count(i) == 1:
            uniq.append(i)
    
    return (
        (len(set(povtor)) == 1) and
        (len(uniq) == 3) and
        (povtor[0]**3 < uniq[0] * uniq[1] * uniq[2])
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)