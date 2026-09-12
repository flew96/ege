f = open(r"variants\25104799\17\17____23447 (1).txt")

data = [int(i) for i in f]

max_el_39 = -10**6
for i in data:
    if (1000 <= abs(i) <= 9999) and (abs(i) % 100 == 39):
        max_el_39 = max(max_el_39, i)


def check(row: list):
    count = 0
    for i in row:
        if 1000 <= abs(i) <= 9999:
            count += 1
    
    return (
        (count == 1) and
        (sum(row)**2 <= max_el_39**2)
    )

count = 0
max_sum = -10**6
for i in range(len(data) - 1):
    row = data[i:i+2]
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)