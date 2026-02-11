def greet():     #function definition
    print("Hello")
greet()    #function call

def greet(name):  #Parameter
    print(f"Hello {name}")
greet("Bhavika") #Argument

def func():
    a = 10
    b = 15
    add = a+b
    return add
print(func()) #output -> 25

#Function without return keyword
def func():
    a = 10
    b = 5
    add = a + b
    print(add)
print(func()) # output will be: # 15 None

# *args allows function to accept any number of positional arguments as a tuple
def add(*args):
    total = 0
    for x in args:
        total += x
    return total


print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4)) # it can take any number of arguments

# **kwargs allow function to accept any number of keyword arguments as a dictionary
def info(**kwargs):
    print(kwargs)
info(name="bhavika", age=20)
