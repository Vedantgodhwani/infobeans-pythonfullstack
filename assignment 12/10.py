s = input()
i = 0 
j = 0 
k = 10 
for char in s:
    n = int(char)
    if n == 0:
        i = i + 1
    j = j + n
    if n < k:
        k = n

n = (i + j) * k
s_flag = 0
if n < 2:
    s_flag = 1
else:
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            s_flag = 1
            break

print("Zero Count =", i)
print("Sum =", j)
print("Smallest Digit =", k)
print("Final Result =", n)
if s_flag == 0:
    print("Prime")
else:
    print("Not Prime")
