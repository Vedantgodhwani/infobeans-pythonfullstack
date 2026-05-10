original = int(input())

reverse = 0
temp = original
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10

diff = original - reverse
if diff < 0:
    diff = -diff

digit_count = 0
if diff == 0:
    digit_count = 1
else:
    temp_diff = diff
    while temp_diff > 0:
        digit_count += 1
        temp_diff //= 10

print(f"Reverse = {reverse}")
print(f"Difference = {diff}")
print(f"Digits = {digit_count}")

if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")