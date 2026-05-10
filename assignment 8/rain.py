soil_moisture = int(input("Enter Soil Moisture (%): "))
temperature = int(input("Enter Temperature (°C): "))
crop_type = input("Enter Crop Type (wheat/other): ").lower()
rainfall_prediction = input("Is rain expected? (yes/no): ").lower()

if soil_moisture <= 30:
    if temperature >= 35:
        if crop_type == "wheat":
            status = "High Water Supply"
        else:
            status = "Moderate Supply"
    else:
        status = "Moderate Supply"

elif soil_moisture <= 60:
    if rainfall_prediction == "yes":
        status = "Delay Irrigation"
    else:
        status = "Light Irrigation"

else:
    status = "No Irrigation"

print(f"Irrigation Decision = {status}")