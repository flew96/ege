#net_ip
mask = "255.252.0.0"
host_ip = "196.83.34.67"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '111111 00', '00000000', '00000000']
['11000100', '010100 11', '00100010', '01000011']

answ = ['11000100', '01010011', '11111111', '11111110']

print(sum([int(i, 2) for i in answ]))
#answ = 788