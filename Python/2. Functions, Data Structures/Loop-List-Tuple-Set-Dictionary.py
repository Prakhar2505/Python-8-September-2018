# 15 September
# for i in range(0, 3):
#     for j in range(0, i+1):
#         print("*", end='')
#     print()

# built in datatypes
# list
# list_var = [1, 2, 3, 'ABC', 87.23, 'ace']
# print(list_var)

# list_var.append(923)
# print(list_var)

# print(list_var[2:])

# list comprehension/slicing
# print(list_var[4:8])

# Here are the list elements : [87.23, 'ace', 923]
# print("Here are the list elements : " + str(list_var))

# tuple
# tuple_var = (1, 2, 'abc', 823.3)
# print(tuple_var)

# var = list((1, 2, 3, 'abc', 'def'))
# print(var)

# set
# set_var = {1, 2, 23, 4, 9, 12, 10}
# print(set_var)

# set_var = {1, 'a', 2, 'b', 4, 'ab', 12, 'abc'}
# print(set_var)
# set_var = {'a', 1, 2, 3, 4, 10}
# print(set_var)


# set_var_int = {1, 2, 3, 5, 4, 6}
#
# set_var_string = {1, 2, 'a', 3, 'b', 'c'}
#
# print(set_var_int.difference(set_var_string))
#
# print(set_var_string.difference(set_var_int))


# dictionary
dict_var = {
    'Name' : 'Himanshu',
    'College' : 'UPES',
    'Address' : 'Dehradun'
}
# print(dict_var)

dict_var['new_member'] = 'Tyagi'
# print(dict_var)

print(dict_var['College'])
