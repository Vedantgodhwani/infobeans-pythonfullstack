num = int(input("Enter number: "))
all_even = True
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        all_even = False
    num = num // 10
if all_even == True:
    print("All Even")
else:
    print("Not All Even")