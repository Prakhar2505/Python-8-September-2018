import numpy as np

# Change False to True to see Numpy arrays in action
if False:
    pythonList = [1, 2.66, 'Hello World', 'abc', 5]
    print(pythonList)

    numpyArray = np.array(pythonList, float)
    print(numpyArray)

    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print(array)

'''
You can index, slice, and manipulate a Numpy array much like you would with a
a Python list.
'''
# Change False to True to see array indexing and slicing in action
if False:
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    print(array[1])
    print("")
    print(array[:2])
    print("")
    array[1] = 5.0
    print(array[1])

# Change False to True to see Matrix indexing and slicing in action
if False:
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print(two_D_array)
    print("")
    print(two_D_array[1][1])
    print("")
    print(two_D_array[1, :])
    print("")
    print(two_D_array[:, 1])

'''
Here are some arithmetic operations that you can do with Numpy arrays
'''
# Change False to True to see Array arithmetics in action
if False:
    array_1 = np.array([1, 2, 3], float)
    # print(array_1.sum())
    array_2 = np.array([5, 2, 6], float)
    print(array_1 + array_2)
    print("")
    print(array_1 - array_2)
    print("")
    print(array_1 * array_2)

# Change False to True to see Matrix arithmetics in action
if False:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print(array_1 + array_2)
    print("")
    print(array_1 - array_2)
    print("")
    print(array_1 * array_2)

if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print(np.mean(array_1))
    print(np.mean(array_2))
    print("")
    print(array_1 * array_2)
    print(np.dot(array_1, array_2))

if False:
    age = [30, 24, 34, 21, 61, 35, 27, 60, 55, 40, 38, 51, 47, 34, 28, 30, 40]

    np_age = np.array(age)

    print(np_age[np_age > 35])


# array = np.array([1, 2, 3])
# array2 = np.array([1, 2, 3])
#
# result_array = array * array2
# # result_array = np.dot(array, array2)
#
# print(result_array)