while True:
    A=int(input("Enter your first number :"))
    B=int(input("Enter your second number :"))
    a=input("Which operation do you want to perform out of (+,-,/,*,//)")
    if (a=='+'):
        print("The addition of two numbers is :",A+B)
    elif (a=='-'):
        print("The subtraction of two numbers is :",A-B)
    elif (a=='*'):
        print("The multiplication of two numbers is :",A*B)
    elif (a=='/'):
        print("The division of two numbers is :",A/B)
    elif (a=='//'):
        print("The absolute division of two numbers is :",A//B)
    choice = input("Do you want to run again? (y/n): ")

    if choice.lower() != "y":
        print("Program ended.")
        break