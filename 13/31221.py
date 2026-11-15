#net_ip 
mask = "255.255.248.0"
host_ip = "64.237.228.143"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11111 000', '00000000']
['01000000', '11101101', '11100 100', '10001111']

answ = ['01000000', '11101101', '11100000', '00000000']

print(sum([int(i, 2) for i in answ]))
