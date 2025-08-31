N=int(input("Enter your number :"))
if (N>100)and(N%5==0):
    print(f"The number you entered {N} is greater than 100 as well as divisible by 5.")
elif (N==100):
    print(f"Your number {N} is equal to 100")
elif (N<100)and (N%5!=0):
    print(f"The number {N} is neither greater than 100 nor divisible by 5")
elif(N<100):
    print(f"Your number {N} is divisible by 5 but smaller than 100")
else:
    print(f"Your number {N} is greater than 100 but not divisible by 5")
