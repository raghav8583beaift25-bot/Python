A=int(input("Enter your number :"))
if A>10 and A<50:
    print(f"A={A} lies between 10 and 50")
elif A<=10 or A>=50:
    print("It does not lie in between 10 and 50")
else:
    print("Please enter a valid number ")