amount=int(input("Enter annual income:"))
if amount<=250000:
	print("no tax")
elif amount<=500000:
	tax=amount*.05
	print(f"tax={tax}")
elif amount<=1000000:
	tax=amount*.20
	print(f"tax={tax}")
elif amount>=1000000:
	tax=amount*.30
	print(f"tax={tax}")
