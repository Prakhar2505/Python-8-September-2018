## Regular for loop

# Question - Print 'Hello World' 3 times.

# for i in range(3, 0):
#     print("Hello World")

## for loop

## basic for loop, with incrementation of 1
# for i in range(0, 10):
#     print(i)

## reverse for loop
# for i in range(10, 0,-1):
#     print(i)

# *
# * *
# * * *

# for i in range(0, 3):
#     for j in range(0, i+1):
#         print("*", end='')
#     print()

# 1
# 1 2
# 1 2 3

# for i in range(1, 4):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# times = int(input('Enter how many numbers you want to check.'))
# for i in range(0, times):
#     number = int(input('Enter the number.'))
#     if (number%2 == 0):
#         print('Even number')
#     else:
#         print('Odd number')

# for i in range(0, 3):
#     for j in range(0, i+1):
#         print("*", end=' ')
#     print()

# for i in range(0, 5):
#     if (i<=2):
#         for j in range(1, i+1):
#             print("-", end = ' ')
#         for k in range(3, i, -1):
#             print("*", end= ' ')
#     if (i>=3):
#         for j in range(i, 4):
#             print('-', end=' ')
#         for k in range(3, i+2):
#             print("*", end=' ')
#     print()

## Nested Loops
# for i in range(0, 3):
#     for j in range(0, i+1):
#         print("*", end="")

# **********************************
# for i in range(1, 5):
#     print("Hello World")
#
#     for j in range(0, 2):
#         print("Inisde j")
#
# ################################
# for j in range(4, 9):
#     for i in range(0, i):
#         print("Hello World")
#     print("Hello")
# ##########################
# for i in range(0, 3):
#     for j in range(0, i+1):
#         print("*", end="_")
#     print()