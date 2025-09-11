# LIST
# A list in python is an ordered, mutable and indexed collection that allows duplicates.
# It is written in []square brackets.
# can store mixed data types.(string,float,int,long etc)

# my_list=[10,20,30,40,50,"Neeraj"]
#  Hashcode Value
# print(my_list)
# Index 
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# for items in my_list:
#     print(items)

# Updating the list elements
# my_list[5]="Spider-Man"
# print(my_list)

# Adding elements in list
# my_list.append("Shine")
# print(my_list)

# Inserting elements
# my_list.insert(2,"Vishal")
# print(my_list)

# Removing specific Element
# my_list.remove(40)
# To delete a Element at specific index
# del my_list[5]
# To print length of list
# print(len(my_list))

# nums=[5,3,2,1,9,10,15,17]
# print("The list in Ascending order is ",nums.sort())
# nums.sort()
# print("The list in ascending order is ",nums)
# nums.sort(reverse=True)
# print("The list in descending order is ",nums)
# nums.reverse()
# print(nums)

# Slicing or Indexing
# nums=[5,3,2,1,9,10,15,17]
# print(nums[0:6:1])
# print(nums[0:6:2])
# print(nums[6:0:-1])

# nums=[10,20,4,45,78,99,20,34,78]
# print("Second Largest is",second_largest(nums))

# To reverse without using in built function
# def reverse_list(list):
#     return list[::-1]
# nums=[1,2,3,4,5]
# print("Reversed list is",reverse_list(nums))