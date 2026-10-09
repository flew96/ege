f = open(r"practice tests/25145224/9/9.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    uniq = []
    repeatable = []

    for i in row:
        if row.count(i) == 3:
            repeatable.append(i)
        else:
            uniq.append(i)

    return (
        (len(uniq) == 1) and
        (len(set(repeatable)) == 2) and
        (len(repeatable) == 6) and
        (sum(set(repeatable)) <  uniq[0]**2)
    )

index = 0
sum_indexes= 0
count_indexes = 0
for row in data:
    index += 1

    if check(row):
        count_indexes += 1
        sum_indexes += index

print(sum_indexes / count_indexes)