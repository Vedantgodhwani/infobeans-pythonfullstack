
amount=int(input("enter the amount"))
if amount>5000:
	discount=amount*.20
	final=amount-discount
	print(f"final amount :{final}")
elif amount<=5000:
	discount=amount*.10
	final=amount-discount
	print(f"final amount :{final}")
elif amount>2000:
	discount=amount*.05
	final=amount-discount
	print(f"final amount :{final}")

