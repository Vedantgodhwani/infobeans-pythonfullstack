current = int(input("Current floor: "))
dest = int(input("Destination floor: "))

if current < dest:
    for i in range(current, dest + 1):
        if i == dest:
            print(i)
        else:
            print(i, end=" → ")
elif current > dest:
    for i in range(current, dest - 1, -1):
        if i == dest:
            print(i)
        else:
            print(i, end=" → ")
else:
    print("Already on the same floor")