n = int(input())
if n < 2:
    print("Not Prime")
else:
    k = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            k = 1
            break
    if k == 0:
        print("Prime Number")
    else:
        print("Not Prime")