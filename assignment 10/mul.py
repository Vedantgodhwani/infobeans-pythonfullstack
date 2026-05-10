start = int(input())
end = int(input())
count = 0

for i in range(start, end + 1):
    if i % 5 == 0:
        count = count + 1

print("Count =", count)