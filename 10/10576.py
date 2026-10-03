mask = "255.255.240.0"

bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)