f = open(r"practice tests\shkolkovo\17\17-1.txt")

data = [int(i) for i in f]

max_el_7 = -10**6
for i in data:
    if abs(i) % 10 == 7:
        max_el_7 = max(max_el_7, i)

def check(row: list):
    count = 0
    for i in row:
        if abs(i) % 10 == 7 and 100 <= abs(i) <= 999:
            count += 1
    
    return (
        (str(abs(row[0]))[0] == str(abs(row[1]))[0] == str(abs(row[2]))[0]) and
        (count >= 1) and
        (abs(sum(row)) < max_el_7)
    )

count = 0
max_sum = -10**6
for i in range(len(data) - 2):
    row = data[i:i+3]
    
    if check(row):
        count += 1
        max_sum = max(max_sum, abs(sum(row)))

print(count, max_sum)