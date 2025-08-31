# NESTED LOOPING
# for i in range (1,4):
#     for j in range (1,4):
#         print(i*j,end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range (i):
#         print("*",end=" ")
#     print()

# for i in range (1,6):
#     for i in range (i):
#         print(i,end=" ")
#     print()

# n=1
# for i in range (0,6):
#     for j in range (i):
#         n+=1
#         print(n-1,end=" ")
#     print()

# rows=5
# for i in range (rows,0,-1):
#     for j in range (i):
#         print("*",end=" ")
#     print()

n=5 
for i in range (1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range (i):
        print("*",end="")
    print()