num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=" ")
elif num1 > num2:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")
else:
    print("Both numbers are same")