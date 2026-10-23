net_ip = "68.203.243.87"
mask = "255.255.224.0"
#host_ip 

bin_net_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)
print(bin_net_ip)

['11111111', '11111111', '111 00000', '00000000']
['01000100', '11001011', '111 10011', '01010111']

answ = ['01000100', '11001011', '11111111', '11111110']

print([int(i, 2) for i in answ])
[68, 203, 255, 254]