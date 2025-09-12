A=[1,4,6,2,31,21,9]
B=int(input("Enter your number :"))
if B in A:
    print(f"B={B} is in list A")
else:
    print(f"B={B} is not in list A")
C=int(input("Enter your number :"))
if C not in A:
    print(f"C={C} is not in list A")
else:
    print(f"C={C} is in list A")