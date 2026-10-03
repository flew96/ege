net_ip = "122.21.48.0"
#mask 
host_ip = "122.21.49.91"

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_net_ip)
print(bin_host_ip)

