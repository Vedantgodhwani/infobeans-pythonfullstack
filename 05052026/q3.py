"""3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if."""
   

e=int(input("enter experiece"))
bonus= "30%" if e>10 else "20%" if e>5 else "10%"
print("bonus",bonus)