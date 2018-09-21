# Creating a normal function in python
def function_name():
    print("Hello World")

function_name()

# Creating a parameterized function in python
def sum(a,b):
    var_3 = a + b
    print(var_3)

var_1, var_2 = 10, 20
sum(var_1, var_2)

# Creating a parameterized function with default values
def sum(a = 2, b = 3):
    var_3 = a + b
    print(var_3)

var_1, var_2 = 10, 20

sum(a=var_1)

# Polymorphism using *
a, b, c = 10, 20, 30

def sum(*args):
    result = 0
    for arg in args:
        result = result + arg
    print(result)

sum(a,b,c)

