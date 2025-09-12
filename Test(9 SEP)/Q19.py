list=[2,3,4,5,6,7,8,9,0,1]
i=int(input("Enter a number of your choice :"))
for item in list:
    if item==i:
        print(f"The item i={i} you searched has been found")
        break
else:
        print("The item is not in the list")