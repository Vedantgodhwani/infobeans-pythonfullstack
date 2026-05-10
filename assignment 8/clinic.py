age = int(input("Enter age: "))
severity = input("Severity (critical/moderate/low): ").lower()
insurance = input("Insurance (insured/uninsured): ").lower()

if severity == "critical":
    if age >= 60:
        print("Treatment = immediate ICU")
    else:
        print("Treatment = Emergency ward")

elif severity == "moderate":
    if insurance == "insured":
        print("Treatment = priority treatment")
    else:
        print("Treatment = general queue")

elif severity == "low":
    if age < 10:
        print("Treatment = pediatric priority")
    else:
        print("Treatment = wait")
