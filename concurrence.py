num = int(input("Number: "))
digit_to_find = int(input("Digit: "))
count = 0
while num > 0:
    if num % 10 == digit_to_find:
        count = count + 1
    num = num // 10
print(count)