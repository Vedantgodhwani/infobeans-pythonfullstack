num_str = input("Enter Number: ")
digits = [int(d) for d in num_str]

if len(digits) < 2:
    print("Need at least 2 digits.")
else:
    initial_gap = abs(digits[0] - digits[1])
    print(f"Initial Gap = {initial_gap}")
    
    is_consistent = True
    i = 0
    while i < len(digits) - 1:
        current_gap = abs(digits[i] - digits[i+1])
        if current_gap != initial_gap:
            is_consistent = False
            break
        i += 1
    
    if is_consistent:
        print("Consistent Pattern")
    else:
        print("Pattern Break Detected")