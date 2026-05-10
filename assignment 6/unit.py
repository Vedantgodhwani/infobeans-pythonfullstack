units=int(input("units"))
if units<=100:
    print("usage category = normal usage")
elif units>=300:
    print("usage category =high usage")
elif units>=200:
    print("usage category =moderate usage")
elif units<100:
    print("usage category=low usage")