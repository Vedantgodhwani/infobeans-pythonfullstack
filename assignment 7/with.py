balance=int(input("enter balance"))
if balance<1000:
	print("Withdrawl not allowed")
elif balance<=5000:
	print("Maximum withdrawl limit:₹1000")
elif balance>5000:
	print("maximum withdrawl limit :₹5000")