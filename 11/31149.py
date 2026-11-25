from math import ceil, floor, log2

for x in range(1, 10_000):
    length = 440
    i = ceil(log2(x))
    data_of_one_id = ceil(length*i/8)
    
    if data_of_one_id*1892412 >= 305726*1024:
        print(x)
        break