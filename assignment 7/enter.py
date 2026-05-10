marks = int(input("Enter Marks: "))
entrance_score = int(input("Enter Entrance Score: "))
category = input("Enter Category (general/other): ").lower()

if marks >= 70:
    if entrance_score >= 80:
        if category == "general":
            status = "Admitted"
        else:
            status = "Admitted with Scholarship"
    else:
        if marks >= 85:
            status = "Admitted under Management Quota"
        else:
            status = "Rejected"

elif category != "general" and marks >= 60:
    if entrance_score >= 70:
        status = "Waitlist"
    else:
        status = "Rejected"

else:
    status = "Rejected"

print(f"Admission Status = {status}")