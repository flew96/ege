num = (
    5*1764**2025 + 4*74088**2026 + 2*42**7 - 2022
)

count = 0
while num > 0:
    if (num % 42) % 2 == 1:
        count += 1
    num //= 42

print(count)