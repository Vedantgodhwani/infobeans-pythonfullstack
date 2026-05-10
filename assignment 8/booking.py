cls = input("Enter class (business/economy): ").lower()
distance = int(input("Distance: "))
booking_time = input("Booking (early/late): ").lower()

if cls == "business":
    if distance < 1000:
        print("Ticket price = 8000")
    else:
        print("Ticket price = 5000")

elif cls == "economy":
    if distance > 1000:
        if booking_time == "early":
            print("Ticket price = 4000")
        else:
            print("Ticket price = 5000")
    else: 
        print("Ticket price = 2500")
        
else:
    print("Invalid class entered.")