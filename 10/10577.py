host1 = "10.96.180.231"
host2 = "10.96.140.118"

bin_host1 = [bin(int(i))[2:].zfill(8) for i in host1.split(".")]
bin_host2 = [bin(int(i))[2:].zfill(8) for i in host2.split(".")]

print(bin_host1)
print(bin_host2)

['00001010', '01100000', '1 0110100', '11100111']
['00001010', '01100000', '1 0001100', '01110110']