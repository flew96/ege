f = open(r"9\5284\5284.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    uniq = []
    repeatable = []
    
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
        else:
            uniq.append(i)
    
    return (
        ((max(row) + min(row))**2 > (sorted_row[1]**2 + sorted_row[2]**2 + sorted_row[3]**2 + sorted_row[4]**2)) or
        (len(repeatable) == 3)
    )

count = 0
for row in data:
    if check(row):
        count += 1
        
print(count)