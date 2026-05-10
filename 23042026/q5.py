5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome

n=int(input("enter the number "))
temp=n
rev=0
while n>0:
	rem=n%10
	rev=(rev*10)+rem
	n=n//10
if temp==rev:
	print("pallindrome")
else:
	print("non pallindrome")