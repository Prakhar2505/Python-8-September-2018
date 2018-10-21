import pandas as pd

titanic_data = pd.read_csv('data/train.csv')

pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 100)
# print(titanic_data.describe())

## display the data
# print(titanic_data)

## print all lines and columns of the dataset.
# pd.set_option('display.max_columns', 15)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_rows', 891)
# print(titanic_data)

## print the count of all the rows and columns in the dataset.
# print(titanic_data.shape)
# rows = titanic_data.shape[0]
# columns = titanic_data.shape[1]
# print("Total number of rows, columns in the data set are: ", rows, ", ", columns)

## print all the columns in the dataset.
# print(titanic_data.describe())

## print all the columns name in a list, with their datatype.
# new_data = {}
# new_data['Column'] = titanic_data.columns
# print("List of columns in our data set is: ", new_data['Column'])
# #
# new_data['Data Type'] = titanic_data.dtypes
# print("Datatypes of the columns are as follows - ", new_data['Data Type'])
# #
# # print all the columns name and check if they contain any null value and sum those null values.
# print(titanic_data.isnull().any())
#
# # print only the column names that contain any null value
# null_value_columns_pos = [x for x in range(len(new_data['Column'])) if titanic_data.iloc[:,x].isnull().any()]
# print("Positions of columns that contain null values are - ", null_value_columns_pos)
#
# null_value_columns_name = [titanic_data.columns[x] for x in range(len(new_data['Column'])) if titanic_data.iloc[:,x].isnull().any()]
# print("Names of the columns that contain null values are - ", null_value_columns_name)

################
# Univariate Analysis

##################
## Continuous variables

## age variable

## display the data using box plot, to analyze the outliers
import matplotlib.pyplot as plt
import seaborn as sea
sea.boxplot(data=titanic_data['Age'])
plt.show()

## getting the outliers value
# quantile1 = titanic_data['Age'].quantile(0.25)
# quantile3 = titanic_data['Age'].quantile(0.75)
#
# inter_quantile_range = quantile3 - quantile1
#
# lower_limit = quantile1 - (1.5 * inter_quantile_range)
# upper_limit = quantile3 + (1.5 * inter_quantile_range)
# print("Q1: ", quantile1, "\nQ3: ", quantile3, "\nInter Quantile Range: ", inter_quantile_range,
#       "\nLower Limit: ", lower_limit, "\nUpper Limit: ", upper_limit)
#
# clean_list = [titanic_data['Age'][x] for x in range(len(titanic_data['Age'])) if (not pd.isnull(titanic_data['Age'][x]))]
# print("Clean list: ", clean_list)
#
# outliers = [clean_list[x] for x in range(len(clean_list))
#             if (not((clean_list[x]>lower_limit) and (clean_list[x]<upper_limit)))]
#
# print("Outlier values are: \n", outliers)

##############
# Assignment
# 1. Perform the univariate analysis on PClass, SibSp, Parch, Fare
# 2. Understand what does all the columns depict.
# 3. Understand the distribution of Fare.
