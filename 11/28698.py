from math import ceil, log2

res = []
for amount_of_users in range(1, 10000000):
    lenght = 23
    i = 7
    
    data_of_one_user = ceil(lenght*i/8) + 15
    
    if data_of_one_user*amount_of_users <= 300*1024**2:
        res.append(amount_of_users)

print(max(res))