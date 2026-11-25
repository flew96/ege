from math import ceil, log2

i = 12
data_per_ind = ceil(i*173/8)

print(1048576*data_per_ind/1024**2)