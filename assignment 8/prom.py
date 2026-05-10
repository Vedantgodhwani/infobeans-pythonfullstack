experience = int(input("Enter Experience (years): "))
rating = int(input("Enter Rating (1-5): "))
projects = int(input("Enter Projects Completed: "))
salary = int(input("Enter Current Salary: "))

if experience >= 5:
    # Path for experienced employees
    if rating >= 4:
        if projects >= 3:
            if salary <= 50000:
                status = "Promoted with 30% hike"
            else:
                status = "Promoted with 20% hike"
        else:
            status = "Promoted with 10% hike"
    else:
        status = "No promotion"

else:
    if rating == 5:
        status = "Fast track promotion"
    else:
        status = "No promotion"

print(f"Promotion Status = {status}")