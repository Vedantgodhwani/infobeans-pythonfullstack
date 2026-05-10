distance = int(input("Enter distance: "))
cls = input("Enter class (sleeper/AC): ").lower()
if distance <= 100:
    if cls == "sleeper":
        print("Total fare = 100")
    elif cls == "ac":
        print("Total fare = 200")

elif distance <= 500:
    if cls == "sleeper":
        print("Total fare = 300")
    elif cls == "ac":
        print("Total fare = 600")

else: 
    if cls == "sleeper":
        print("Total fare = 500")
    elif cls == "ac":
        print("Total fare = 1000")