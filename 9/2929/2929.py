f = open(r"9\2929\2929.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        ((max(row) + min(row)) / 2) <= sorted_row[1]
    )


count = 0
for row in data:
    if check(row):
        count += 1
        
print(count)