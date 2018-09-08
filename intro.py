first_number = 10
second_number = 20

third_number = first_number + second_number

print(third_number)
print("First number is: ", first_number)
print("Second number is: %d" % second_number)
print("Result of two number is: " + str(third_number))

# TODO: regarding datatype or class
print((third_number))

first_number, second_number = second_number, first_number
print(first_number)
print(second_number)