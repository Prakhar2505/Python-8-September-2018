import pandas as pd

# Question: Why do we use series in panda.
# Series is a one dimensional object, that can hold any type of data such as int, float and string.

# Change False to True to create a Series object
if False:
    series = pd.Series(['Gurjas', 'Python', 'Brillica', 123])
    print(series)

    # output:
    # 0   Gurjas
    # 1   Python
    # 2   Brillica

# Change False to True to see custom index in action
if False:
    series = pd.Series(['Gurjas', 'Python', 'Brillica'],
                       index=['Instructor Name', 'Course', 'Company Name'])
    print(series)
    print("Instructor name is: ", series['Instructor Name'])

# Change False to True to see boolean indexing in action
if True:
    cuteness = pd.Series([1, 2, 3, 4, 5],
                         index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print(cuteness)
    # print(cuteness > 3)
    # print("")
    print(cuteness[cuteness > 3])
