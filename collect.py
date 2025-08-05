#Lists are used to store multiple items in a single variable
#Lists are created using square brackets:
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

empty_list = []
the_list = ["apple", "banana", "cherry", "grapes", "watermelon"]

print(f"len(the_list)")
print(f"get_value: {the_list [0]}")

print(f"type(the_list)")

list1 = ["apple" , "banana", "cherry", "grapes", "watermelon"]
list2 = [0, 2, 4, 1,]
list3 = [True, False, False]
print(f"list2,{list1 [False]}")

the_list.append("orange")
print(f"Add elements: {the_list}")
#The remove() method removes the specified item.
the_list.pop(1)
print(f"the_list")

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
my_dict = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  : 1964,
  "colors" : ["red", "white", "blue", "black"]
}
print(f"Dict: {my_dict}  | {type(my_dict)}")
print(f"Accessing my_dict(brand)")

#Tuples are used to store multiple items in a single variable
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuple items are ordered, unchangeable, and allow duplicate values.
my_tuple = ("apple", "banana", "cherry")
print(f"Tuple: {my_tuple} | Data type: {type(my_tuple)}")
print(f"Accessing : {my_tuple[2]}")
