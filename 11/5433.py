from math import log2, ceil

for len_of_adress in range(1, 10000):
    data_per_user = ceil((48+5+4+10+5*len_of_adress)/8)
    
    if data_per_user*1316 <= 27*1024:
        print(len_of_adress)