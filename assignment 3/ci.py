p = float(input("Principal = "))
r = float(input("Rate = "))
t = float(input("Time = "))
amount = p * (1 + r / 100)**t
ci = amount - p
print(f"Amount = {amount}")
print(f"Compound Interest = {ci}")