n = int(input())
i = n + 1
while True:
    k = 0
    if i < 2:
        k = 1
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                k = 1
                break
    if k == 0:
        print("Next Prime =", i)
        break
    i = i + 1
