num_str = input("Enter Number: ")
break_pos = -1

for i in range(len(num_str) - 1):
    if not (int(num_str[i+1]) > int(num_str[i])):
        break_pos = i + 2 # Position is 1-based index of the digit that broke the rule
        print(f"Break at position = {break_pos}")
        print("Not Increasing Number")
        break
else:
    print("Strictly Increasing Number")