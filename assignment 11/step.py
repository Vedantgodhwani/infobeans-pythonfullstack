num = int(input())
temp = num

num_digits = 0
copy_num = num
while copy_num > 0:
    num_digits += 1
    copy_num //= 10

sum_diff = 0
max_diff = 0
diff_string = ""

temp = num
while temp > 9:
    d1 = temp % 10
    d2 = (temp // 10) % 10
    
    step = d1 - d2
    if step < 0:
        step = -step
        
    sum_diff += step
    
    # Check for largest
    if step > max_diff:
        max_diff = step
        
    diff_string = str(step) + " " + diff_string
    temp //= 10

print(f"Step Differences: {diff_string.strip()}")
print(f"Sum = {sum_diff}")
print(f"Largest = {max_diff}")

if sum_diff % num_digits == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")