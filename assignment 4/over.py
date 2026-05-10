r = 275
o = 48.3
b = (int(o) * 6) + round((o % 1) * 10)
rr = r / (b / 6)
print(f"Total Balls: {b}")
print(f"Run Rate: {rr}") # Removed :.2f