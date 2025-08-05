#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function
def my_function():
  print("This is my function")
def other_function():
  print("This is another function")

my_function()
other_function()

#Function with parameters
def my_full_name(fname, lname):
    print("The name is: {fname} {lname}")

    my_full_name("Tatiana", "McCray")
    #print_full_name("lname= McCray", fname= "Tatiana")


    #Functions that return something
    def get_full_name(fname, lname):
        return "{fname} {lname}"
    
    full_name = get_full_name("Tatiana", "McCray")
    print(full_name)
