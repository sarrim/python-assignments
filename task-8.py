# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)
        

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# print(map(my_list*2, my_list))

x = lambda my_list : my_list * 2

print(x(my_list))