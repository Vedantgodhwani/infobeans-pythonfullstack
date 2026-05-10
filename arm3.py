num = int(input("Enter 3-digit number: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes = sum_of_cubes + (digit * digit * digit)
    temp = temp // 10
if num == sum_of_cubes:
    print("Armstrong")
else:
    print("Not Armstrong")