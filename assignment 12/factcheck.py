n = int(input())
k = 0 # Factor count
s = -1 # Smallest factor
for i in range(1, n + 1):
    if n % i == 0:
        k = k + 1
        if i > 1 and s == -1:
            s = i

if k > 2:
    print("Composite Number")
    print("Factors Count =", k)
    print("Smallest Factor =", s)
else:
    print("Not Composite")