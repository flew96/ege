#net_ip 
mask = "255.192.0.0"
host_ip = "146.180.173.153"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11 000000', '00000000', '00000000']
['10010010', '10 110100', '10101101', '10011001']

answ = ['10010010', '10111111', '11111111', '11111110']
print(sum([int(i, 2) for i in answ]))