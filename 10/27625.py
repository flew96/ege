net_ip = "172.16.96.0"
mask = "255.255.224.0"
#host_ip 

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)
print(bin_net_ip)

['11111111', '11111111', '111 00000', '00000000']
['10101100', '00010000', '011 00000', '00000000']

count = 0
for i in range(2**13):
    if bin(i)[2:].count("1") % 2 == 0:
        count += 1

print(count)