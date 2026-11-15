#net_ip 
mask = "255.255.255.0"
host_ip = "102.162.200.51"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11111111', '00000000']
['01100110', '10100010', '11001000', '00110011']

answ = ['01100110', '10100010', '11001000', '11111110']
print(sum([int(i, 2) for i in answ]))