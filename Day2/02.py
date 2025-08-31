A=int(input("Enter your marks :"))
if(A>=90 and A<=100):
    print("You scored A+ grade")
elif(A>=75 and A<90):
    print("You scored A grade")
elif(A>=60 and A<75):
    print("You scored B grade")
elif(A>=40 and A<60):
    print("You scored c grade")
elif(A>=0 and A<40):
    print("You failed your exam")
else:
    print("Your marks are invalid")
# 2nd method
# A=int(input("Enter your marks :"))
# if(A>=100 or A<=0):
#     print("Your marks are invalid")
# elif(A>=90 and A<=100):
#     print("You scored A+ grade")
# elif(A>=75 and A<90):
#     print("You scored A grade")
# elif(A>=60 and A<75):
#     print("You scored B grade")
# elif(A>=40 and A<60):
#     print("You scored c grade")
# else:
#     print("You failed your exam")