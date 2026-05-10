num = int(input())
square = num * num
digit_sum = 0

while square > 0:
    digit = square % 10
    digit_sum = digit_sum + digit
    square = square // 10

if digit_sum == num:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet.")