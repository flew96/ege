f = open(r"practice_tests/25200944/9/9.txt")

data = [
    [int(i) for i in row.split()]for row in f
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
        (len(repeatable) == 5) and
        (len(set(repeatable)) == 2) and
        (len(uniq) == 2) and
        ((sum(uniq)/2) > min(repeatable))
    )

count = 0
for row in data:
    if check(row):
        count += 1

print(count)