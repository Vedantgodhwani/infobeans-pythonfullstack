username=input("enter username:")
password=input("enter password:")
if username=="admin":
    print("valid user")
else:
    print("invalid user")

if len(password)>=8:
    print("strong password")
else:
    print("weak password")