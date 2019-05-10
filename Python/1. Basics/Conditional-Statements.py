# conditional statements

# 1. if condition
if (var1==10):
    print("Yes it's value is 10.")
    print("Hello World")
print("Python Programming")
print("Out of if")

# 2. if-else condition
var1 = var1+1
if (var1==10):
    print("Yes it's value is 10.")
    print("Hello World")
else:
    print("No it's not equal to 10.")
print("Python Programming")
print("Out of if")

# 3. else-if condition
print(var1)
if (var1==10):
    print("Yes it's equal to 10.")
    print("Hello")
elif(var1<10):
    print("Yes it's less than 10.")
    print("World")
else:
    print("Yes it's greater than 10.")
print("Hello Programming")

# take input from the user
value = int(input('Enter the value'))
# print(value)
value = value + 12
print(value)

# swap two numbers in one line
first_number = 10
second_number = 20

first_number, second_number = second_number, first_number
print("Value are : ", first_number, second_number)