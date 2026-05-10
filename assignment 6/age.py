age = int(input("Age = "))
show_time = input("Show Time (morning/evening) = ").lower()
day_type = input("Day (weekday/weekend) = ").lower()
if age < 18:
    if show_time == "morning":
        price = 100
    else:
        price = 150
else:
    if show_time == "evening":
        if day_type == "weekend":
            price = 300
        else:
            price = 250
    else:
        price = 200
print(f"Ticket Price = {price}")