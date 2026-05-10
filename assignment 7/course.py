course = input("Enter course category (Programming/Design/Marketing): ").lower()
user_type = input("Enter user type (Student/Professional/Other): ").lower()
if course == "programming":
    fee = 5000
elif course == "design":
    fee = 4000
elif course == "marketing":
    fee = 3000
else:
    fee = 0
    print("Invalid course category.")

if fee > 0:
    if user_type == "student":
        discount = 0.20
    elif user_type == "professional":
        discount = 0.10
    else:
        discount = 0.00
    final_fee = fee - (fee * discount)
    print(f"Final Course Fee: ₹{final_fee:.0f}")