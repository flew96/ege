#net_ip
mask = "255.224.0.0"
host_ip = "73.148.145.65"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '111 00000', '00000000', '00000000']
['01001001', '100 10100', '10010001', '01000001']

answ = ['01001001', '10011111', '11111111', '11111110']
print([int(i, 2) for i in answ])