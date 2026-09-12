f = open(r"17\21416\17_21416.txt")

data = [int(i) for i in f]

sum_neg = 0
for i in data:
    if i < 0:
        sum_neg += i
        
def check(row: list):
    return (
        (max(row) * min(row) > sum_neg)
    )

count = 0
max_sum_el = 0
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum_el = max(max_sum_el, sum(row))

print(count, max_sum_el)