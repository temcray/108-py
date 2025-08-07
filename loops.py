#A for loops is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
the_list = ["apple", "banana", "cherry", "grapes", "watermelon"]

for i in the_list:
  print(i)

  for x in "banana":
    print(x)
  #keyword continue and break
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    #break
    continue
  print(fruits)
    
#he range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for my_list in range(3,len("my_list"),2):
  print("my_list[numbers]")