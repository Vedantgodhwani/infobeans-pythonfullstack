num_str = input("Enter Number: ")
digits = [int(d) for d in num_str]
n = len(digits)

# Pre-allocate list with zeros
products = [0] * (n - 1)
total_sum = 0

for i in range(n - 1):
    prod = digits[i] * digits[i+1]
    products[i] = prod
    total_sum += prod

if products:
    smallest = products[0]
    for p in products:
        if p < smallest:
            smallest = p
else:
    smallest = 0

print(f"Products: {' '.join(map(str, products))}")
print(f"Sum = {total_sum}")
print(f"Smallest = {smallest}")

if total_sum % n == 0:
    print("Stable Number")
else:
    print("Unstable Number")