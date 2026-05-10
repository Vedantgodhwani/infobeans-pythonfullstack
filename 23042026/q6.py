#6. Armstrong Number (3-digit)
#In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
#Write a program to **check whether a number is an Armstrong number using loops**.

#Input: 153
#Output: Armstrong

n=int(input("enter the number"))
temp=n
sum=0
while n>0:
	rem=n%10
	sum=sum+(rem**3)
	n=n//10
if sum==temp:
print("armstrong number")
else:
print("non armstrong")