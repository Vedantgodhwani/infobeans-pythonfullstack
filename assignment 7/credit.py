salary = int(input("Enter Monthly Salary: "))
credit_score = int(input("Enter Credit Score: "))
existing_loans = int(input("Enter Number of Existing Loans: "))

if salary >= 30000:
    if credit_score >= 750:
        if existing_loans == 0:
            risk = "Low Risk"
        elif existing_loans <= 2:
            risk = "Medium Risk"
        else:
            risk = "High Risk"
    else:
        if salary >= 50000:
            if credit_score >= 650:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
        else:
            risk = "High Risk"
else:
    risk = "Not Eligible"
print(f"Risk Level = {risk}")