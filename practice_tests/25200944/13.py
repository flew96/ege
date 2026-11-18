host_ip = "148.92.138.52"
mask = "255.255.192.0"

bin_host_ip = [bin(int(i))[2:].zfill(8) for i in host_ip.split(".")]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split(".")]

print(bin_mask)
print(bin_host_ip)

['11111111', '11111111', '11000000', '00000000']
['10010100', '01011100', '10001010', '00110100']
['10010100', '01011100', '10______', '________']

count = 0
left = '100101000101110010'
for i in range(2**14):
    right = bin(i)[2:].zfill(14)

    ip = left+right
    if (ip.count("1") % 3 == 0):
        count += 1

print(count)

print(int("1000010011011", 2))