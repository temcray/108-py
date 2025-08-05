print("Hello World from python")
print(2)
print(5+3)
print(True)
#Create a variable
name = "Tatiana"
age = 36
last_name = "McCray"
found = False
print(name)

#Concatenation
print("My name is: " + name + ", and I'm " +  str(age) + " years old.")
print("Did he showed up to the class?" + str(found))

#The f format
#f"" or f""""""

print(f"My name is {name} and I am {age} years old.")
print(f"""
text
text
{name}      
                      im still in the f format
I like Web Developing""")
#The type() function helps you to know the data type of the variable
print(type(name))
print(type(age))
print(type(True))

#Casting
#Help us to convert different data types
#str() - convert from any data type to string
#int() - convert string number to Numeric values
print(20+int("20"))
print(20+age)
print(20+int(2.98))
print(20+float("2.98"))

#input method
#is going to allow us to interact with the terminal and pass some values
#input()
#print(input())
#print(input("Enter you name here: "))
#new_age =int(input("Enter a new age: "))
#print(str(age + new_age)) # 36 + 30 = 56
                           # 36 + 44 = 80
x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(x+y)



