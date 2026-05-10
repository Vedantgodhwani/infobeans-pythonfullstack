p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
a = p * (1 + r/100)**t
print(f"Amount after interest = {a}")