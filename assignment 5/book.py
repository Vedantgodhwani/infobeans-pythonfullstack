membership=input("membership active (yes/no)").lower()
books=int(input("enter number of books"))
if membership=="yes":
    print("entry allowed")
if books<3:
    print("can issue more books")
