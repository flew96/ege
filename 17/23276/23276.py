f = open(r"17\23276\17_23276.txt")

data = [int(i) for i in f]

max_el_25 = -10**6
for i in data:
    if abs(i) % 100 == 25:
        max_el_25 = max(max_el_25, i)

def check(row: list):
    count = 0
    for i in row:
        if 1000 <= abs(i) <= 9999:
            count += 1
    
    return (
        (count <= 2) and
        (sum(row) <= max_el_25)
    )

count = 0
max_sum_el = -10**6    
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))
        
print(count, max_sum_el)