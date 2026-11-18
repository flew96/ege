f = open(r"practice tests\25210936\17\17.txt")

data = [int(i) for i in f]

count = 0
for i in data:
    if 10 <= i <= 99:
        count += 1


def check(row: list):
    
    return (
        (row[0] % 1237 == count) or
        (row[1] % 1237 == count)
    )

counter = 0
max_sum = 0
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))
        
print(counter, max_sum)