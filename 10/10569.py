#net_ip
mask = "255.255.224.0"
host_ip = "10.8.248.131"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '111 00000', '00000000']
['00001010', '00001000', '111 11000', '10000011']

answ = ['00001010', '00001000', '11100000', '00000000']
print([int(i, 2) for i in answ])