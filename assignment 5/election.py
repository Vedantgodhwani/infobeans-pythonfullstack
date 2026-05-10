age = int(input("Enter age: "))
id = input("Do you have ID (yes/no): ").lower()

if age >= 18:
    print("Eligible to vote")
if id == "yes":
    print("Allowed inside booth")