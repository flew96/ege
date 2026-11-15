#net_ip 
mask = "255.255.224.0"
host_ip = "68.203.243.87"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '111 00000', '00000000']
['01000100', '11001011', '111 10011', '01010111']

answ = ['01000100', '11001011', '11111111', '11111110']
print(sum([int(i, 2) for i in answ]))