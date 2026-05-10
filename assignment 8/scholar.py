marks = int(input("marks: "))
income = int(input("enter income: "))
category = input("enter category (scst/obc/general): ").lower()

if marks >= 85:
    if income <= 300000 and category != "general":
        print("Scholarship = Full scholarship")
    else:
        print("Scholarship = 75% scholarship")
elif 70 < marks <= 84:
    if income <= 200000:
        print("Scholarship = 50% scholarship")
    else:
        print("Scholarship = 25% scholarship")

if marks<=70:
    print("Scholarship = No scholarship")