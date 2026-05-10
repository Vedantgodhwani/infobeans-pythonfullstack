#9. Check All Digits Are Even**
# machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
#Write a program to **check whether all digits of a number are even using loops**.

#Input: 2468
#Output: All Even

#Input: 2456
#Output: Not All Even


n = int(input("Enter the number: "))

while n > 0:
    rem = n % 10
    if rem % 2 != 0:
        print("Not All Even")
        break
    n //= 10
else:
    print("All Even")