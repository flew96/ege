net_ip = "154.201.192.0"
#mask
host_ip = "154.201.208.17"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_host_ip)
print(bin_net_ip)

['10011010', '11001001', '11010000', '00010001']
['10011010', '11001001', '11000000', '00000000']
answ = ['11111111', '11111111', '11100000', '00000000']

print([int(i, 2) for i in answ])