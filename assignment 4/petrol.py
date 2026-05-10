d = float(input("Distance (km): "))
m = float(input("Mileage (km/l): "))
p = float(input("Price per litre: "))
used = d / m
cost = used * p
py print(f"Petrol Used = {used} litres")
print(f"Total Cost = {cost}")