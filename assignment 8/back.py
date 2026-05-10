marks = 78
backlog = 0
project = 85

if marks >= 75:
    if backlog == 0:
        if project >= 80:
            print("Result = First Class with Distinction")
        else:
            print("Result = First Class")
    else:
        print("Result = First Class")
elif 60 <= marks <= 74:
    if backlog <= 2:
        print("Result = Second Class")
    else:
        print("Result = Pass Class")
elif 50 <= marks <= 59:
    print("Result = Pass")
else:
    print("Result = Fail")