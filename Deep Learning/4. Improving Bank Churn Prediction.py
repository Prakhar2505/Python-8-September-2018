# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
dataset.head()
X = dataset.iloc[:, 3:13]
X
y = dataset.iloc[:, 13]
y

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

#X_values = X.values
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X_values = onehotencoder.fit_transform(X_values).toarray()
#X_values = X_values[:, 1:]

## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 40)

## Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
#
## Part 2 - Now let's make the ANN!
#
## Importing the Keras libraries and packages
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


### Making predicitons regarding specific person 
##Geography: France
##Credit Score: 600
##Gender: Male
##Age: 40 years old
##Tenure: 3 years
##Balance: $60000
##Number of Products: 2
##Does this customer have a credit card ? Yes
##Is this customer an Active Member: Yes
##Estimated Salary: $50000
#
#print(geographyEncoder.inverse_transform([0, 1, 2]))
#print(gender_encoder.inverse_transform([0, 1]))
#
#
#
#person_characteristics = np.array([[0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])
#
#print("Values: ", X_train.iloc[1])
#
#predict_customer = classifier.predict([person_characteristics])
#predict_customer = (predict_customer > 0.5 )
#print("Predictions for single customer is: ", predict_customer)

## Part 4 - Improving our ANN

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from keras.models import Sequential
from keras.layers import Dense

def buildClassifier(optimizer):
    classifier = Sequential()
    classifier.add(Dense(output_dim = 6, init = 'uniform', activation='relu', input_dim = 10))
    classifier.add(Dense(output_dim = 6, init = 'uniform', activation='relu'))
    classifier.add(Dense(output_dim = 1, init = 'uniform', activation='sigmoid'))
    classifier.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics=['accuracy'])
    return classifier

classifier = KerasClassifier(build_fn = buildClassifier)
parameters = {'batch_size': [10, 15, 25, 30, 40],
              'nb_epoch': [100, 200, 500],
              'optimizer': ['adam', 'rmsprop']}

grid_search = GridSearchCV(estimator = classifier,
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 10)

grid_search = grid_search.fit(X_train, y_train)
best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_

print("Best parameters: ", best_parameters)
print("Best accuracy: ", best_accuracy)

#best_classifier = classifier.fit(X_train, y_train, batch_size = 25, epochs = 100)
best_classifier = buildClassifier(optimizer='adam')
best_classifier.fit(x=X_train, y=y_train, batch_size=25, epochs=100)
best_prediction = best_classifier.predict(X_test)

best_prediction = (best_prediction>0.5)
best_score = accuracy_score(y_test, best_prediction)
print("Best score is: ", best_score)

best_confusion_matrix = confusion_matrix(y_test, best_prediction)
best_confusion_matrix


























    













