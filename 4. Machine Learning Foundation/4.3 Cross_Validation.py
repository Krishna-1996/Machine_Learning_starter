# 4.3 Cross_Validation: K-Fold cross validation
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

#Load data from csv file 
data = pd.read_csv("E:/Machine Learning/Machine Learning/house_prices.csv")

# convert the dataset into binary 0 or 1 for better understanding by MAchine model
data = pd.get_dummies(data, columns=['mainroad'])
data = pd.get_dummies(data, columns=['guestroom'])
data = pd.get_dummies(data, columns=['basement'])
data = pd.get_dummies(data, columns=['hotwaterheating'])
data = pd.get_dummies(data, columns=['airconditioning'])
data = pd.get_dummies(data, columns=['prefarea'])
data = pd.get_dummies(data, columns=['furnishingstatus'])
X = data.drop('price', axis = 1).values
prices = data['price'].values


#Initialize K-Fold cross validation
num_flods = 5
kf = KFold(n_splits=num_flods)
fold_mse = []

#Loop through the folds
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = prices[train_index], prices[test_index]

    #create and train the Linear Regression
    model = LinearRegression()
    model.fit(X_train,y_train)
    
    #Make prediction on the test 
    y_pred = model.predict(X_test)

    # Calculate mean square error for this fold
    mse = mean_squared_error(y_test, y_pred)
    fold_mse.append(mse)

#Calculate average mean square error of all across the folds
average_mse = sum(fold_mse)/num_flods

#Print the result
print("Mean Square Error for each folds: ", fold_mse)
print("Average Mean Square Error: ", average_mse)








