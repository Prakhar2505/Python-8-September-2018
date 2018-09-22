# taking input from the users.
# understanding the use of lambda

var1 = int(input('Enter the value of first variable: '))
var2 = int(input('Enter the value of second variable: '))

formula = lambda var1, var2: var1 * var2

print("Multiplication result of these numbers is: ", formula(var1, var2))

# understanding the use of filter
# find the numbers divisible by 2 in the list.

list_var = [10, 30, 23, 87, 92, 13, 34, 44, 69]

even_numbers = lambda x: x%2 == 0

result = filter(even_numbers, list_var)
print(list(result))
#
#
# # mapping values -
#
week_number = [1, 2, 3, 4, 5, 6, 0, 6, 5, 2, 3]
#
dictionary = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    0 : 'Sunday'
}
#
# def fun(week):
#     return dictionary.get(week)
#a

condition = lambda x: dictionary.get(x)
#
result = list(map(condition, week_number))
# #
print(result)
#
# # Understanding reduce function
from functools import reduce

list_var = [1, 2, 3, 4, 5, 7, 6]

condition = lambda x, y: x*y

result = reduce(condition, list_var)
print(result)

# List Comprehension
# list comprehension

# print the square root of all the odd numbers from 1 to 10.
# list_var = []
#
# for i in range(1, 11, 2):
#     list_var.append(i)
#
# print(list_var)
#
# square_list = [x**2 for x in range(1, 40, 5)]
# print(square_list)

# Quiz - generate a new list using list comprehension.
list_var = [x for x in range(0, 11)]
print(list_var)


# Quiz - we have 3 dogs and 4 persons, print a pair for all the possible combinations.
# Quiz - find all the pairs of 'Labra Dog' only and save them into new list.

