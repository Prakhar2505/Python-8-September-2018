list_var = ['abc', 12, 24832.9, 2432, 'ace']

print(list_var)

tuple_var = ('abc', 12, 24832.9, 2432, 'ace')

print(tuple_var)

list_var.append('Ankit')
print(list_var)

# print the element at 3 position
print(tuple_var[2])
# slicing
print(tuple_var[1:4])

print(tuple_var[:1])

# Write a program to initialize a list, tuple variable without any element.
list_var = []
tuple_var = ()

a = 10
print(list_var)
print(tuple_var)
print(a)

# to initialize a list or tuple
a = tuple((10, 20, 'abc'))
print(a)

if (isinstance(a[1], str)):
    print('String')
else:
    print('Not string')


# set
set_var = {'12', 234, 8974, 43.88, 'abc'}
print(set_var)

# dictionary
dictionary_var = {
    'name': 'Gurjas Singh',
    'age': 25,
    'location': 'Dehradun'
}
print(dictionary_var)

# using key name
print(dictionary_var['name'])

# using object or object oriented
print(dictionary_var)