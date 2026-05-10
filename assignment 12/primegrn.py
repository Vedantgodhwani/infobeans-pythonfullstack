n = int(input())
i = n + 1
while True:
    k = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            k = 1
            break
    if k == 0:
        print("Next Prime ID =", i)
        print("Gap =", i - n)
        break
    i = i + 1