net_ip = "122.21.48.0"
#mask 
host_ip = "122.21.49.91"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_net_ip)
print(bin_host_ip)

['01111010', '00010101', '00110000', '00000000']
['01111010', '00010101', '00110001', '01011011']
['11111111', '11111111', '11111110', '00000000']
