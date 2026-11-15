net_ip = "172.16.160.00"
mask = "255.255.240.0"
#host_ip 

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_net_ip)
print(bin_mask)

['10101100', '00010000', '1010 0000', '00000000']
['11111111', '11111111', '1111 0000', '00000000']

count = 0
left = "10101100000100001010"
for i in range(2**12):
    a = left + bin(i)[2:]
    if a.count("1") % 2 == 0:
        count += 1
print(count)