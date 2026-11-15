#net_ip 
mask = '255.255.192.0'
host_ip = '154.141.198.190'

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11 000000', '00000000']
['10011010', '10001101', '11 000110', '10111110']

answ = ['10011010', '10001101', '11111111', '11111111']

print(sum([int(i, 2) for i in answ]))