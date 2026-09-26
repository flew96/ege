#net_ip = 
mask = "255.224.0.0"
host_ip = "11.92.135.56"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]
bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '111 00000', '00000000', '00000000']
['00001011', '010 11100', '10000111', '00111000']

answ = ['00001011', '01011111', '11111111', '11111110']
print([int(i, 2) for i in answ])
