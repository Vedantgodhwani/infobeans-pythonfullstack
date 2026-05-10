s = input()
n = 0
for i in s:
    n = n + int(i)
k = 0
if n < 2:
    k = 1
else:
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            k = 1
            break

print("Sum =", n)
if k == 0:
    print("Lucky Number")
else:
    print("Normal Number")