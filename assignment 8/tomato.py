order_amount = int(input("Enter Order Amount: "))
customer_type = input("Enter Customer Type (VIP/Regular): ").lower()
payment_method = input("Enter Payment Method (online/cash): ").lower()

if order_amount >= 2000:
    if customer_type == "vip":
        if payment_method == "online":
            offer = "Free Dessert + 20% Discount"
        else:
            offer = "Free Dessert"
    else:
        if order_amount >= 5000:
            offer = "15% Discount"
        else:
            offer = "10% Discount"

elif order_amount >= 1000:
    if customer_type == "vip":
        offer = "10% Discount"
    else:
        offer = "5% Discount"

else:
    
    offer = "No Offer"

print(f"Offer = {offer}")