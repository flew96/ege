from math import ceil, log2

for lenght in range(1, 10000):
    i = 7
    data_of_one_id = ceil(lenght*i/8)
    
    if data_of_one_id*5895222 > 23*1024**2:
        print(lenght)
        break