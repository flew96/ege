f = open(r"practice_tests/25200946/9/9.txt")

data = [
    [int(i) for i in row.split()]for row in f
]

def check(row: list):
    uniq = []
    repeatable = []
    sorted_row = sorted(row)
    for i in row:
        if row.count(i) > 1:
            repeatable.append(i)
        else:
            uniq.append(i)

    return (
        (len(repeatable) == 3) and
        (len(set(repeatable)) == 1) and
        (len(uniq) == 4) and
        (2*(max(row) + min(row)) >= sum(sorted_row[1:6]))
    )

num = 0
for row in data:
    num += 1
    if check(row):
        print(num)

#answ = 9960