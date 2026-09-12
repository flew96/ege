f = open(r"17\21903\17_21903.txt")

data = [int(i) for i in f]

min_el_15 = 10**6
for i in data:
    if abs(i) % 100 == 15 and 100 <= abs(i) <= 999:
        min_el_15 = min(min_el_15, i)

def check(row: list):
    return (
        ((row[0] < 0 and row[1] < 0 and row[2] < 0) or 
        (row[0] > 0 and row[1] > 0 and row[2] > 0)) and 
        (min(row) * max(row) > min_el_15**2)
    )

count = 0
min_mult = 10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        min_mult = min(min_mult, max(row) * min(row))

print(count, min_mult)