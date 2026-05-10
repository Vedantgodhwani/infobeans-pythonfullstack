vehicle = input("Enter vehicle type (Bike/Car/Bus): ").lower()
hours = int(input("Enter hours parked: "))

if vehicle == "bike":
    rate = 10
elif vehicle == "car":
    rate = 20
elif vehicle == "bus":
    rate = 50
else:
    rate = 0
    print("Invalid vehicle type.")

if rate > 0:
    total_fee = rate * hours
    
    if hours > 5:
        total_fee += 100
        
    print(f"Total Parking Fee: ₹{total_fee}")