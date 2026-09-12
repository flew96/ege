f = open(r"17\28938\17_28938.txt")

data = [int(i) for i in f]

max_el_28 = -10**6
for i in data:
    if abs(i) % 100 == 28:
        max_el_28 = max(max_el_28, i)

def check(row: list):
    count = 0
    sum = 0
    
    for i in row:
        if 100 <= abs(i) <= 999:
            count += 1
        sum += i
    
    return (
        (count >= 1) and
        (max_el_28 > sum / 3 > 0) 
    )

count = 0
max_sum_el = 0
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))
        
print(count, max_sum_el)