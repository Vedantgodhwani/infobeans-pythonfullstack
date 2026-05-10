s = input()
i = -1 
j = 10
for k in s:
    n = int(k)
    if n > i:
        i = n
    if n < j:
        j = n

n = i + j
s = 0 
if n < 2:
    s = 1
else:
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            s = 1
            break

print("Largest =", i)
print("Smallest =", j)
print("Sum =", n)
if s == 0:
    print("Prime")
else:
    print("Not Prime")