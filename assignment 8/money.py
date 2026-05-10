transaction_amount = int(input("Enter Transaction Amount: "))
location = input("Enter Location (domestic/international): ").lower()
otp_verified = input("Is OTP verified? (yes/no): ").lower()
account_age = int(input("Enter Account Age (years): "))
unusual_activity = input("Unusual activity detected? (yes/no): ").lower()

if transaction_amount >= 10000:
    if location == "international":
        if otp_verified == "yes":
            status = "Allowed"
        else:
            status = "Blocked"
    else:
        if transaction_amount >= 50000:
            if account_age >= 2:
                status = "Allowed"
            else:
                status = "Flagged"
        else:
            status = "Allowed"

else:
    if unusual_activity == "yes":
        status = "Flagged"
    else:
        status = "Allowed"

print(f"Transaction Status = {status}")