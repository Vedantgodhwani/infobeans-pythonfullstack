start, end = map(int, input().split())
count = 0
for i in range(start, end + 1):
    if i % 7 == 0:
        count += 1
print(f"Count = {count}")