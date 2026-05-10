cart=int(input("enter cart value:"))
usertype=input("usertype(premium/regular:").lower()
discount=cart-(cart*0.20)
disc=cart-(cart*.10)
if usertype=="premium":
    print(f"final amount,{discount}")
elif usertype=="regular":
    print(f"final amount , {disc}")