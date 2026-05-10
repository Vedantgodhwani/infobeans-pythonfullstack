num = int(input())
odd_count = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        odd_count = odd_count + 1
    num = num // 10

print("Odd Digits Count =", odd_count)