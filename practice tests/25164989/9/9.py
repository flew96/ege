f = open(r"practice tests\25164989\9\9.txt")

data = [[int(i) for i in row.split()] for row in f
        ]

def check(row: list):
    sorted_row = sorted(row)
    
    return (
        (len(set(row)) == len(row)) and
        ((min(row) + max(row))*2 == (sum(sorted_row[1:4])))
    )


count = 0
for row in data:
    if check(row):
        count += 1
print(count)