mask = "255.255.240.0"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)

['11111111', '11111111', '1111 0000', '00000000']