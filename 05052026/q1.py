"""1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only."""


amount = int(input("Enter purchase amount: "))
customer_type = input("Enter customer type (premium/regular): ").lower()
if customer_type == "premium":
    disc_percent = 0.20 if amount > 5000 else 0.10
elif customer_type == "regular":
    disc_percent = 0.10 if amount > 3000 else 0.05
else:
    disc_percent = 0
    print("Invalid customer type!")
discount_amt = amount * disc_percent
final_payable = amount - discount_amt

print(f"Discount applied: {disc_percent * 100}%")
print(f"Total discount: {discount_amt}")
print(f"Final payable amount: {final_payable}")