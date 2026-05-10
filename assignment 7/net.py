usage=int(input("enter daily data usage"))
if usage>3:
	print("Recommended plan: premium plan ")
elif usage<=3:
	print("recommended plan:tandard plan")
elif usage<1:
	print("Recommended plan:basic plan")