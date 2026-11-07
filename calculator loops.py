while 1:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")

    choice=input("enter your choice:")
    if choice=="5":
        print("calculator closed!")
        break
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
    if choice=="1":
        print(a+b)
    elif choice=="2":
        print(a-b)
    elif choice=="3":
        print(a*b)
    else:
        print(a/b)