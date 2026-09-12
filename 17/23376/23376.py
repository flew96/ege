f = open(r"17\23376\17_23376.txt")

data = [int(i) for i in f]

max_el_37 = -10**6
for i in data:
    if 10000 <= abs(i) <= 99999 and abs(i) % 100 == 37:
        max_el_37 = max(max_el_37, i)


def check(row: list):
    count = 0
    for i in row:
        if 10000 <= abs(i) <= 99999:
            count += 1
    
    return (
        (count == 1) and 
        (sum(row)**2 > max_el_37**2)
    )

count = 0
max_sum_el = 0
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)