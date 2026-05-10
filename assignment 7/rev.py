salary = int(input("Enter salary: "))
rating = int(input("Enter rating (1-5): "))
if rating == 5:
    rev = salary * 1.25  
    print(f"Revised salary: {rev}")
elif rating == 4:
    rev = salary * 1.20
    print(f"Revised salary: {rev}")
elif rating == 3:
    rev = salary * 1.10
    print(f"Revised salary: {rev}")
elif rating == 2:
    rev = salary * 1.05
    print(f"Revised salary: {rev}")
elif rating == 1:
    rev = salary * 1.00  
    print(f"Revised salary: {rev}")
else:
    print("Invalid rating entered.")