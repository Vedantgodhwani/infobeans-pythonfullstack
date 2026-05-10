
speed=int(input("enter speed"))
time=int(input("enter time in hours"))
minute=int(input("enter time in minutes"))
total= ((time*60)+(minute*1))/60
print(f"total time ={total} hours")
distance=speed*total
print(f"distance ={distance} kms"		)
