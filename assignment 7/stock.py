stock = int(input("Enter Stock Level: "))
priority = input("Enter Priority Level (high/low): ").lower()
distance = int(input("Enter Delivery Distance (km): "))

if stock >= 100:
    if priority == "high":
        if distance <= 200:
            status = "Dispatch Immediately"
        else:
            status = "Dispatch via Fast Courier"
    else:
        if stock >= 300:
            status = "Bulk Dispatch"
        else:
            status = "Normal Dispatch"

elif stock >= 50:
    if priority == "high":
        status = "Partially Dispatch"
    else:
        status = "Hold"

else:
    status = "Out of Stock"

print(f"Dispatch Status = {status}")