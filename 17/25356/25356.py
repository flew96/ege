f = open(r"17\25356\17_25356.txt")

data = [int(i) for i in f]

max_el_30 = -10**6
for i in data:
    if abs(i) % 100 == 30:
        max_el_30 = max(max_el_30, i)

def check(row: list):
    flag = True
    for i in row:
        if 1000 <= abs(i) <= 9999:
            flag = False
    
    return (
        (flag) and 
        (sum(row) > max_el_30)
    )


count = 0
max_el_sum = -10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_el_sum = max(max_el_sum, sum(row))

print(count, max_el_sum)