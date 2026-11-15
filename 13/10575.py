net_ip = "118.193.24.0"
#mask
host_ip = "118.193.30.139"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_net_ip)
print(bin_host_ip)

['01110110', '11000001', '00011 000', '00000000']
['01110110', '11000001', '00011 110', '10001011']
['11111111', '11111111', '11111 000', '00000000']