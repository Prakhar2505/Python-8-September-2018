# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
dataset.head()
X = dataset.iloc[:, 3:13]
print(X)
Y = dataset.iloc[:, 13]
print(Y)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
geographyEncoder = LabelEncoder()
X['Geography'] = geographyEncoder.fit_transform(X['Geography'])
geography_classes = geographyEncoder.classes_
print(geography_classes)


gender_encoder = LabelEncoder()
X['Gender'] = gender_encoder.fit_transform(X['Gender'])
gender_classes = gender_encoder.classes_
print(gender_classes)

## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 40)

#import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model

## Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu', input_dim = 10))

# Adding the second hidden layer
classifier.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Visualizing keras model
#plot_model(classifier, to_file='neural_model.png')

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Checking accuracy
from sklearn.metrics import accuracy_score
clf_score = accuracy_score(y_test, y_pred)
print("Accuracy Score is:", clf_score)




























    













