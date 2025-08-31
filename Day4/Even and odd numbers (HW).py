N=int(input("Enter the number which you want to use :"))
if (N%2)==0 and N>=0:
    print(f"The number {N} you entered is Even.")
elif (N%2)!=0 and N>=0:
    print(f"The number {N} you entered is Odd.")
else:
    print("The number you entered is negative integer.\nPlease enter a positive number.")