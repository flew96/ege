f = open(r"17\27629\17_27629.txt")

data = [int(i) for i in f]

arr = []
for i in data:
    if len(str(abs(i))) == 4 and abs(i) % 100 == 43:
        arr.append(i)

end_43 = max(arr)

def check(row: list):
    return (
        (len(str(abs(row[0]))) == 4 or len(str(abs(row[1]))) == 4) and 
        (sum(row)**2 < end_43**2)
    )



count = 0
max_sq = 0
for i in range(len(data) - 1):
    row = data[i:i+2]
    
    if check(row):
        count += 1
        max_sq = max(max_sq, sum(row)**2)

print(count, max_sq)