price=int(input("enter the price of mobile"))
downpayment=int(input("enter the amount of downpayment"))
interest=0.10*downpayment
months=int(input("enter the time duration in months"))
remaining =price-downpayment
amwi=+remaining+remaining*.10
emi=amwi/months
print("Monthly EMI",emi)
 