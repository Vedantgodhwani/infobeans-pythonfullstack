s = input()
i = 0 
j = 0 
for k in s:
    n = int(k)
    if n % 2 == 0:
        i = i + 1
    else:
        j = j + 1

n = i - j
if n < 0:
    n = -n

k = 0 
if n < 2:
    k = 1
else:
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            k = 1
            break

print("Even Count =", i)
print("Odd Count =", j)
print("Difference =", n)
if k == 0:
    print("Prime")
else:
    print("Not Prime")