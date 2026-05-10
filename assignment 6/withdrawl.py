balance = int(input("balance="))
withdrawl = int(input("withdrawl amount"))
PIN = input("pin status(correct/incorrect): ").lower()
if balance == withdrawl:
    print("check withdrawl limit")
if withdrawl >= 10000:
    print(f"PIN={PIN}")
if PIN == "correct":
    print("Transaction Successful")
else:
    print("Invalid pin")
if withdrawl <= 10000:
    print("Limit exceeded")
if balance < withdrawl:
    print("Insuffecient balance")