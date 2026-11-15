#net_ip
mask = "255.255.224.0"
host_ip = "191.89.109.206"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '111 00000', '00000000']
['10111111', '01011001', '011 01101', '11001110']

answ = ['10111111', '01011001', '01111111', '11111110']
print(sum([int(i, 2) for i in answ]))