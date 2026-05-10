temp=int(input("Enter temperature:"))
if temp<=0:
	print("Weather condition :freezing")
elif temp<=20:
	print("weather condition :cold")
elif temp<=35:
	print("weather condition : Warm")
elif temp>35:
	print("weather condition : Hot")