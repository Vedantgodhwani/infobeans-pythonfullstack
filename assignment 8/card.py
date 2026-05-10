income = int(input("enter income: "))
credit = int(input("enter credit score: "))
emp = input("enter employment type (government/private): ").lower()
debt = int(input("enter existing debt: "))

if income <= 50000:
    if credit >= 750:
        if debt < 20000:
            print("Card type = premium card")
        else:
            print("card type = gold card")
    elif credit >= 650: 
        if emp == "government":
            print("Card type = gold card")
        else:
            print("card request rejected")
    else:
        print("card request rejected")
