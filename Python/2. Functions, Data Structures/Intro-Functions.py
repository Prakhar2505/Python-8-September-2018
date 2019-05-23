## basic function


# creating a function
def function_name():
    for i in range(4):
        print("Hello World")

function_name()
print("How are you?")

## passing a value to the function

def fun(value):
    if (value%2 == 0):
        return "Even number"
    else:
        return "Odd number"

var = fun(29)
print(var)



## Question - Create a function that takes 2 values input from the user and perform the following tasks
# 1. Add those values and return the result inside a function.
# 2. Check if that returned value is even or odd.

def sum(a, b):
    result = a+b
    return result

var1 = int(input('Enter the value of first variable:'))
var2 = int(input('Enter the value of second variable:'))
result = sum(var1, var2)
print(result)

if (result%2 == 0):
    print("Even number")
else:
    print("Odd number")



## multiple values

def addition(first, second, *third):
    result = first + second
    for i in range(len(third)):
        result = result + third[i]
    print(result)

addition(10, 20, 40, 30, 10)

## default values
first = int(input('Enter first value'))
second = int(input('Enter second value'))

def divisor(first, second=1):
    result = first/second
    print("Division result is: ", result)

if (second==0):
    print("You have entered second number as 0. It's invalid.")
    divisor(first)
else:
    divisor(first, second)


# ## calling a function with argument name

def division(first_number, second_number):
    result = first_number / second_number
    print("The division result is: ", result)

division(second_number=20, first_number=10)


# create a function that takes two numbers and print their
# multiplication result. The numbers should be float.

def multiplication(first_number, second_number):
    result = first_number * second_number
    print('The multiplication result is: ', result)

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
multiplication(first_number, second_number)
