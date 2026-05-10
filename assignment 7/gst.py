bill=int(input("Enter bill amount"))
if bill<=1000:
	final=bill+(bill*.05)
	print(f"Final bill amount :{final}")
elif bill<=5000:
	final=bill+(bill*.12)
	print(f"Final bill amount:{final}")
elif bill>5000:
	final=bill+(bill*.18)
	print(f"Final bill amount :{final}")
