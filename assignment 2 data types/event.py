time=int(input("enter duration"))
h=time/3600
m=(time%3600)//60
s=time%60 
print("total event duration in seconds:",time)
print("hours:",h)
print("minutes:",m)
print("seconds:",s)