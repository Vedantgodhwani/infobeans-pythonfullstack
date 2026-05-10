age = int(input("Age="))
weight = int(input("Weight="))
goal = input("goal(weight loss/muscle gain:").lower()

if age >= 18:
    if weight >= 80:
        if goal == "weight loss":
            print("Plan=Cardio plan")
        else:
            print("Plan=Strength plan")
    elif weight <= 80:
        print("Plan=General fitness plan")

if age < 18:
    print("not allowed")