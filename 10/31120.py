#net_ip 
mask = "255.255.255.240"
host_ip = "189.163.226.71"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11111111', '1111 0000']
['10111101', '10100011', '11100010', '0100 0111']

answ = ['10111101', '10100011', '11100010', '01000000']
print(sum(int(i, 2) for i in answ))