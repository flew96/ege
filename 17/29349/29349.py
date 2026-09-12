f = open(r"17\29349\17_29349.txt")

data = [int(i) for i in f]

min_el_123 = 10**8
for i in data:
    if abs(i) % 123 == 0 and i > 0:
        min_el_123 = min(min_el_123, i)

def check(row: list):
    return sum(row) < min_el_123

count = 0
max_sum = -10**6
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sum = max(max_sum, sum(row))

print(count, max_sum)