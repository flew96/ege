f = open(r"9\5126\5126.txt")

data = [
    [int(i) for i in row.split()] for row in f
]

def check(row: list):
    repeatable = []
    uniq = []
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
        else:
            uniq.append(i)
    
    return (
        (len(repeatable) == 3) and
        (sum(uniq) / 3 <= sum(repeatable))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)