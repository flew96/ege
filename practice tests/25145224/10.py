net_ip = "192.168.32.64"
mask = "255.255.255.192"
#host_ip

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)
print(bin_net_ip)

['11111111', '11111111', '11111111', '11 000000']
['11000000', '10101000', '00100000', '01 000000']