a=int(input("Enter your First number :"))
b=int(input("Enter your Second number :"))
c=int(input("Enter your Third number :"))
if a > b:
    if a > c:
        print(f"a={a} is the largest:")
    elif a==c:
        print("a is greater than b but equal to c")
    else:
        print(f"c={c} is the largest:")
elif a==b:
    if b>c:
        print("a and b are equal but greater than c.")
    elif b<c:
        print("a and b are equal but smaller than c.")
    else:
        print("All three are equal")
else:
    if b > c:
        print(f"b={b} is the largest:")
    elif b==c:
        print("a is greater than b but b is equal to c")
    else:
        print(f"c={c} is the largest:")
