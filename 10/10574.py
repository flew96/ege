net_ip = "191.173.144.0"
#mask
host_ip = "191.173.145.240"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_net_ip)
print(bin_host_ip)

['10011110', '01110100', '00000000', '00000000']
['10011110', '01110100', '00001011', '10010010']