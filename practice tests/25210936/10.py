net_ip = "254.118.167.59"
mask = "255.255.128.0"


bin_nep_ip = [bin(int(i))[2:].zfill(8) for i in net_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)
print(bin_nep_ip)

['11111111', '11111111', '1 0000000', '00000000']
['11111110', '01110110', '1 0100111', '00111011']

answ = ['11111110', '01110110', '11111111', '11111111']

print(sum([int(i, 2) for i in answ]))

[254, 118, 255, 255]