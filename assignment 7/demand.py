demand = int(input("Enter Demand level (0-100): "))
time_status = input("Enter Time (peak/off-peak): ").lower()
distance = int(input("Enter Distance (km): "))

if demand >= 80:
    if time_status == "peak":
        if distance >= 10:
            multiplier = "2x Fare"
        else:
            multiplier = "1.5x Fare"
    else:
        if demand >= 90:
            multiplier = "1.8x Fare"
        else:
            multiplier = "1.3x Fare"

elif demand >= 50:
    if time_status == "peak":
        multiplier = "1.2x Fare"
    else:
        multiplier = "Normal Fare"

else:
    multiplier = "Normal Fare"

print(f"Fare Multiplier = {multiplier}")