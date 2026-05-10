amount = int(input("Amount = "))
notes100 = amount // 100
remaining = amount % 100
notes50 = remaining // 50
remaining = remaining % 50
notes10 = remaining // 10
print(f"₹100 x {notes100}")
print(f"₹50 x {notes50}")
print(f"₹10 x {notes10}")