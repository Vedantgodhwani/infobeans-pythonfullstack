num = int(input("Enter number: "))
product = 1
while num > 0:
    product = product * (num % 10)
    num = num // 10
print(product)
if product % 2 == 0:
    print("Even")
else:
    print("Odd")