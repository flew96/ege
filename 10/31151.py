#net_ip
mask = "255.255.192.0"
host_ip = "185.249.55.138"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11 000000', '00000000']
['10111001', '11111001', '00 110111', '10001010']

answ = ['10111001', '11111001', '00111111', '11111111']

print(sum([int(i, 2) for i in answ]))

print([int(i, 2) for i in answ])