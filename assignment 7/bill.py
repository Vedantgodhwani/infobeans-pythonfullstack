units=int(input("enter units consumed:"))
if units>=100:
    bill=units*5
    if units <= 200:
        bill = (100 * 5) + (units - 100) * 7
        print(f"bill={bill}")
    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10
        print(f"Total Electricity Bill: ₹{bill}")