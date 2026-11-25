from math import ceil, log2

for x in range(1, 10_000):
    i = ceil(log2(x))
    data_of_one_id = ceil(i*172/8)
    
    if data_of_one_id*187564 <= 39*1024**2:
        print(x)