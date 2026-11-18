f = open(r"practice tests\25164989\17\17_27629 (1).txt")

data = [int(i) for i in f]

max_43_el = -10**6
for i in data:
    if ((1000 <= abs(i) <= 9999) and
        (abs(i) % 100 == 43)):
        max_43_el = max(max_43_el, i)

print(max_43_el)

def check(row: list):
    count = 0
    for i in row:
        if 1000 <= abs(i) <= 9999:
            count += 1
    
    return (
        (count >= 1) and
        (sum(row)**2 < max_43_el**2)
    )

count = 0
max_sum_el = -10**6
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row)**2)

print(count, max_sum_el)