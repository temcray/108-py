#Lists are used to store multiple items in a single variable
#Lists are created using square brackets:
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

empty_list = []
the_list = ["apple", "banana", "cherry", "grapes", "watermelon"]

print(f"Empty List: {empty_list}")
print(f"List: {the_list}")
print(f"List length: get {len(the_list [0])}")
print(f"Retrieving a value: {the_list[0]}")
print(f"Accessing Elements by Negative Indexing: {the_list[-1]}")
print(f"Accessing Elements by ranges[n:n]: {the_list[0:3]}")
# [k:g] where a is the starting index in the array (included) and b is the stopping point (excluding from the list)
print(f"Accessing Elements by ranges[:n]: {the_list[:4]}")
print(f"Accessing Elements by ranges[n:]: {the_list[1:]}")
#Adding elements to the list
the_list.append("strawberry")
the_list.append("orange")
#Remove elements from the list
#the_list.pop(4)
the_list.pop()
print(f"Removing element from list: {the_list}")
the_list.remove("banana")
print(f"Removing element from list using remove method: {the_list}")
the_list.insert(0, "pear")
print(f"Using insert method: {the_list}")
the_list.clear()
print(the_list)
the_list[2] = "blueberry"
print(f"Changing actual values: {the_list}")

list1 = ["apple" , "banana", "cherry", "grapes", "watermelon"]
list2 = [0, 2, 4, 1,]
list3 = [True, False, False]
print(f"list2,{list1 [False]}")



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
print(f"Accessing item using keys: {my_dict["year"]}")
print(f"Dict length: {len(my_dict)}")
print(f"Accessing item using get: {my_dict.get("brand")}")
print(f"Only print the keys: {my_dict.keys()}")
print(f"Only print the values: {my_dict.values()}")
#dictionary["year"] = 1984
my_dict.update({"year":1985})
print(f"Modifying the dictionary: {my_dict}")
my_dict.pop("colors")
print(f"Deleting elements : {my_dict}")

#Tuples are used to store multiple items in a single variable
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuple items are ordered, unchangeable, and allow duplicate values.
my_tuple = ("apple", "banana", "cherry")
print(f"Tuple: {my_tuple} | Data type: {type(my_tuple)}")
print(f"Accessing : {my_tuple[2]}")
modified_tuple = list(my_tuple)
modified_tuple.append("watermelon")
modified_tuple.pop(0)
my_tuple = tuple(modified_tuple)
print(f"Tuple: {my_tuple} | Data type: {type (my_tuple)}")
