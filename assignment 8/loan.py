salary = 50000
age = 30
credit_score = 760
emi = 18000

if salary >= 40000:
    if 21 <= age <= 60:
        if credit_score >= 750:
            if emi <= (0.4 * salary):
                print("Loan Status = Approved at 8%")
            else:
                print("Loan Status = Approved at 10%")
        elif 650 <= credit_score < 750:
            print("Loan Status = Approved at 12%")
        else:
            print("Loan Status = Reject")
    else:
        print("Loan Status = Reject (Age Issue)")
else: # salary < 40000
    if salary >= 25000 and credit_score >= 700:
        print("Loan Status = Approved at 13%")
    else:
        print("Loan Status = Reject")