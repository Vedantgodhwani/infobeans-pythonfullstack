start, end = map(int, input().split())
results = []
for i in range(start, end + 1):
    if i % 10 == 5:
        results.append(str(i))
print(" ".join(results))
