#net_ip
mask = "255.255.248.0"
host_ip = "205.99.68.249"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11111 000', '00000000']
['11001101', '01100011', '01000 100', '11111001']

answ = ['11001101', '01100011', '01000111', '11111110']
print([int(i, 2) for i in answ])