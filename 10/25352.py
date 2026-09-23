#net_ip
mask = "255.255.252.0"
host_ip = "190.202.83.62"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(host_ip)

['11111111', '11111111', '111111 00', '00000000']
['10111110', '11001010', '010100 11', '00111110']

answ = ['10111110', '11001010', '01010011', '11111110']

print([int(i, 2) for i in answ])