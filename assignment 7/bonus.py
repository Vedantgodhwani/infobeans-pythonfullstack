salary=int(input("Enter salary:"))
exp=int(input("Enter years of experience"))
if exp<10:
	bonus=salary*.20
	print(f"Bonus Amount:{bonus}")
elif exp<=10:
	bonus=salary*.10
	print(f"Bonus Amount:{bonus}")
elif exp<=5:
	bonus=salary*.05
	print(f"Bonus Amount:{bonus}")
elif exp<2:
	print("no bonus")