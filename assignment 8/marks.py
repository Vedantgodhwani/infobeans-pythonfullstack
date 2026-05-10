marks = int(input("Marks: "))
at = int(input("Attendance: "))
internal = int(input("Internal: "))
if at < 75:
    print("Result = detained")
elif marks >= 40:
    if internal >= 20:
        print("Result = pass")
    else:
        print("Result = Grace pass")
elif 35 <= marks < 40:
    if internal >= 25:
        print("Result = Reappear")
    else:
        print("Result = fail")
else:
    print("Result = fail")