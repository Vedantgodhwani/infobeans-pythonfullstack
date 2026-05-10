"""1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions"""


while True:
    print("\n1-> check prime number")
    print("2-> check palindrome")
    print("3-> check reverse")
    print("4-> check count")
    print("5-> exit")
    
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            n = int(input("Enter number: "))
            is_prime = True
            if n < 2:
                is_prime = False
            else:
                for i in range(2, (n // 2) + 1):
                    if n % i == 0:
                        is_prime = False
                        break             
            if is_prime:
                print(f"{n} is a Prime Number")
            else:
                print(f"{n} is not a Prime Number")

        case 2:
            n = int(input("Enter number: "))
            temp = n
            num = abs(n) 
            rev = 0
            while num > 0:
                rem = num % 10
                rev = (rev * 10) + rem
                num = num // 10
            
            if temp >= 0 and temp == rev:
                print(f"{temp} is a Palindrome Number")
            else:
                print(f"{temp} is not a Palindrome Number")

        case 3:
            n = int(input("Enter number: "))
            num = abs(n)
            rev = 0
            while num > 0:
                rem = num % 10
                rev = (rev * 10) + rem
                num = num // 10
            
            if n < 0:
                rev = -rev
            print("Reversed Number is:", rev)

        case 4:
            n = int(input("Enter number: "))
            num = abs(n)
            if num == 0:
                count = 1
            else:
                count = 0
                while num > 0:
                    count += 1
                    num = num // 10
            print("Total digits:", count)

        case 5:
            print("Exiting program... Thank you!")
            break 
        case _: 
            print("Invalid choice. Please try again.")
	
