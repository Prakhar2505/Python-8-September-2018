# print star pattern
for i in range(0, 3):
    for j in range(0, i):
        print('*', end='')
    print()

# print star pattern in reverse
for i in range(0, 3):
    for j in range(3, i, -1):
        print('*', end='')
    print()

# taking input from user:
var1 = int(input('Enter the first number: '))
var2 = int(input('Enter the second number: '))

var3 = var1 + var2
print('Sum of two variables is: ', var3)