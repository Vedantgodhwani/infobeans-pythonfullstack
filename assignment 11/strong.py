num = int(input())
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    # Calculate factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total_sum += fact
    temp //= 10

if total_sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")
