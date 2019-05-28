# # Lambda - function - Filter, Reduce, Map


list_var = [10, 34, 15, 52, 15, 67, 32, 18]


# without lambda function
# new_list = []
#
# def list_filter(list_var):
#     for i in list_var:
#         if (i>30):
#             # return i
#             # print(i)
#             new_list.append(i)
#
# list_filter(list_var)
# print(new_list)

# using lambda
new_list = list(filter(lambda x: x>30, list_var))
print(new_list)


# # map
dictionary = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

list_weeks = [7, 2, 8, 1, 3, 1, 4, 5, 0, 2, 1, 0, 4]
list_weekdays = list(map(lambda x:
                         dictionary.get(x, "Not found"),
                         list_weeks))

print(list_weekdays)

# reduce
from functools import reduce

list_var = [9, 3, 2, 43, 9, 232, 34]

multiplication = reduce(lambda x,y : x*y, list_var)
print("Multiplication result is: ", multiplication)
