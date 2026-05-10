n = int(input())
k = 0
if n < 2:
    k = 1
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            k = 1
            break

if k == 0:
    print("Prime Number")
    i = n + 1
    while True:
        s = 0
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                s = 1
                break
        if s == 0:
            print("Next Prime =", i)
            break
        i = i + 1
else:
    print("Not Prime")
    i = n - 1
    while i > 1:
        s = 0
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                s = 1
                break
        if s == 0:
            print("Previous Prime =", i)
            break
        i = i - 1