unit1 = int(input("Unit1 = "))
unit2 = int(input("Unit2 = "))
unit3 = int(input("Unit3 = "))
unit4 = int(input("Unit4 = "))
unit5 = int(input("Unit5 = "))
unit6 = int(input("Unit6 = "))
highest = unit1
if unit2 > highest:
    highest = unit2
if unit3 > highest:
    highest = unit3
if unit4 > highest:
    highest = unit4
if unit5 > highest:
    highest = unit5
if unit6 > highest:
    highest = unit6
print(f"Highest Stock = {highest}")