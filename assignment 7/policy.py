policy_age = int(input("Enter policy age in years: "))
claim_amount = int(input("Enter claim amount: "))
accident_type = input("Enter accident type (minor/major): ").lower()

if policy_age >= 2:
    if claim_amount <= 50000:
        if accident_type == "minor":
            status = "Approved"
        else:
            status = "Approved with Inspection"
            
    elif claim_amount <= 200000:
        if accident_type == "major":
            status = "Approved with Investigation"
        else:
            status = "Rejected"
            
    else:
        status = "Rejected"

else:
    if accident_type == "minor":
        status = "Rejected"
    else:
        status = "Pending Review"
print(f"Final Decision: {status}")