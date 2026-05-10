"""4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if."""


units = int(input("Enter units consumed: "))

total= units * 10 if units > 300 else units * 7 if units > 100 else units * 5

print(f"Total bill amount: ₹{total}")