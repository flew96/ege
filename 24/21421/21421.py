from string import ascii_uppercase, digits 

alph = digits + ascii_uppercase[:2]

f = open(r"24\21421\24_21421.txt").read()

for digit in (digits + ascii_uppercase):
    if digit not in alph:
        f = f.replace(digit, " ")

nums = f.split()

def clean_num(num: str):
    while num and (num[-1] not in alph[::2]):
        num = num[:-1]
    return (num)

# clean_num("111133377711111")

nums = [clean_num(i.lstrip("0")) for i in sorted(nums, key=len, reverse=True)]
for num in nums[:10]:
    print(num)
