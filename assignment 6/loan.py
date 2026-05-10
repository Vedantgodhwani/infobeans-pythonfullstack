salary = int(input("enter salary: "))
creditscore = int(input("enter credit score: "))
loans = int(input("existing loans: "))

if salary >= 30000:
    if creditscore >= 750:
        print("loan approved")
    else:
        print("loan rejected")  
else:
    if loans < 2:
        print("loan status: conditional approval")
    else:
        print("loan rejected")