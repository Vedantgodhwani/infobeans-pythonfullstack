attendance=int(input("Enter attendance percentage"))
if attendance>=75:
	print("status:Eligible")
elif attendance<=74:
	print("Status: eligible with warning")
elif attendance<=60:
	print("Status: Not eligible ")