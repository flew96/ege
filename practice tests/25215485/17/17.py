f = open(r"practice tests/25215485/17/17_31850.txt")

data = [
    int(i) for i in f
]

max_el_23 = -10**6
for i in data:
    if (
        (1000 <= abs(i) <= 9999) and
        (abs(i) % 100 == 23)
    ):
        max_el_23 = max(max_el_23, i)

def check(row: list):
    count = 0
    for i in row:
        if (
            (1000 <= abs(i) <= 9999) and
            (abs(i) % 10 == 1)
        ):
            count += 1

    return (
        (count == 2) and
        (sum(row) > max_el_23)
    )

counter = 0 
max_sum = -10*6
for i in range(len(data) - 2):
    row = data[i:i+3]

    if check(row):
        counter += 1
        max_sum = max(sum(row), max_sum)


print(counter, max_sum)