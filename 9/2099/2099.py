f = open(r"9\2099\2099.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    sorted_row = sorted(row)
    triangle = False
    special_triangle = False
    
    if sum(row) == 180 and (0 not in row):
        triangle = True
        if sorted_row[0] == sorted_row[1] or sorted_row[1] == sorted_row[2]:
            special_triangle = True
    
    if special_triangle:
        return 2
    elif triangle:
        return 1
    return 0

count_triangle = 0
count_special_triangle = 0
for row in data:
    if check(row) == 1:
        count_triangle += 1
    elif check(row) == 2:
        count_triangle += 1
        count_special_triangle += 1

print(count_special_triangle * 100 // count_triangle)