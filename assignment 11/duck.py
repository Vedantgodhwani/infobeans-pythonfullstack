num_str = input()
num = int(num_str)

if num_str[0] == '0':
    print("Not a Duck Number")
else:
    is_duck = False
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0:
            is_duck = True
        temp //= 10
    
    if is_duck:
        print("Duck Number")
    else:
        print("Not a Duck Number")