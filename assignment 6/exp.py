experience = int(input("Experience (years) = "))
rating = int(input("Rating = "))
salary = int(input("Salary = "))
if experience >= 5:
    if rating >= 4:
        if salary < 50000:
            bonus_percentage = 0.20  
        else:
            bonus_percentage = 0.10  
    else:
        bonus_percentage = 0.05  
     bonus_amount = salary * bonus_percentage
    print(f"Bonus = {bonus_amount}")
    
else:
    print("Bonus = 0")