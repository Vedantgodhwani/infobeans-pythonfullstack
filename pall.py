num = int(input("Enter number: "))
original = num
reverse = 0
while num > 0:
    reverse = (reverse * 10) + (num % 10)
    num = num // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")