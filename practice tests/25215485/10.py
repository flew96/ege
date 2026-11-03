net_ip = "145.92.137.192"
#mask 
host_ip = "145.92.137.200"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_net_ip)
print(bin_host_ip)

['10010001', '01011100', '10001001', '1100 0000']
['10010001', '01011100', '10001001', '1100 1000']
['11111111', '11111111', '11111111', '1111 0000']