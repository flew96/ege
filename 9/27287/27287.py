f = open(r"9\27287\27287.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    povtor = []
    uniq = []
    
    for i in row:
        if row.count(i) == 1:
            uniq.append(i)
        elif row.count(i) == 3:
            povtor.append(i)
    
    return ((len(uniq) == 1) and
            (len(povtor) == 6 and
            (uniq[0] <= min(povtor)))
            )


for row in data:
    if check(row):
        print(row)
        break