n = int(input())
if n <= 1:
    print("Not Composite")
else:
    k = 0
    for i in range(2, n):
        if n % i == 0:
            k = 1
            break
    if k == 1:
        print("Composite Number")
    else:
        print("Not Composite")