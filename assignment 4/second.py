s_in = int(input("Total seconds: "))
h = s_in // 3600
rem = s_in % 3600
m = rem // 60
s = rem % 60
print(f"Hours = {h}")
print(f"Minutes = {m}")
print(f"Seconds = {s}")