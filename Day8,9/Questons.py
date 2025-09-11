# 1
# nums=[10,20,4,45,78,99,20,34,78]
# def second_largest(nums):
#     a=list(set(nums))     To remove duplicate elements
#     a.sort()
#     if len(a)<2:
#         return None
#     else:
#         return a[-2]

# 2
# Target Questions
# nums=[1,5,7,-1,5]
# def Find_pairs(list,Target):
#     pairs=[]
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]+list[j]==Target:
#                 pairs.append((list[i],list[j]))
#     return pairs
# Target=6
# print("The pairs with sum",Target,"are",Find_pairs(nums,Target))
