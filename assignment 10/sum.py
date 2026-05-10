num = int(input())
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        total = total + i

print("Sum =", total)