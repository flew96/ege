f = open(r"9\28930\28930.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (row == sorted_row) and
        (len(set(sorted_row)) == len(row)) and
        (min(row) + max(row) <= sum(row) - min(row) - max(row))
    )
    

count = 0

for row in data:
    if check(row):
        count += 1
    
print(count)