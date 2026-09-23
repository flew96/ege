#net_ip 
mask = "255.255.252.0"
host_ip = "192.168.159.86"


bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]


print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '111111 00', '00000000']
['11000000', '10101000', '100111 11', '01010110']

answ = ['11000000', '10101000', '10011100', '00000000']

print(sum([int(i, 2) for i in answ]))
