# 4.2 Model _Evaluation_and_Optimization
'''
A. Accuracy_score
B. Precision_score
C. Recall_score
D. F1_score
'''

print("Different metrics used in Logistic Regression")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# import dataset of heart_disease 
data = pd.read_csv("E:/Machine Learning/Machine Learning/Churn_Modelling.csv")
#print('original data: ')
#print(data)

# convert the dataset into binary 0 or 1 for better understanding 
data = pd.get_dummies(data, columns=['Geography'])
data = pd.get_dummies(data, columns=['Gender'])
#print("after dummy data: ")
#print(data)

#Drop unnecessary columns
colm_to_drops = ['RowNumber', 'CustomerId', 'Surname',]
new_data = data.drop(colm_to_drops,axis = 1)#Entirely drop the column
#print("dropping some data: ")
#print(new_data)


# Sigmoid function:
def sigmoid(z):
    return 1/(1+np.exp(-z))

#If we want to remove/ drop any column(here missing values columns)

# print(new_data.isnull().any()) #(No required as there is no null value)
column_names = list(new_data.columns.values)
#print(column_names)# print all columns name


# Extract features and labels from new_data
features = new_data.drop('Exited', axis=1).values
labels = new_data['Exited'].values

#Split new_data for training and testing purpose
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

#Create and train the Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("METRICS")
# a. ACCURACY SCORE 
acc_scr = accuracy_score(y_test, predicted)
print('a. accuracy_score: ',acc_scr)

# b. PRECISION SCORE
pre_scr = precision_score(y_test, predicted)
print('b. precision_score: ',pre_scr)

# c. RECALL SCORE
recall_scr = recall_score(y_test, predicted)
print('c. recall_score: ',recall_scr)

# D. F1 SCORE
f1_scr = f1_score(y_test, predicted)
print('d. f1_score: ',f1_scr)

# E. Confusion Metrics
conf_metr = confusion_matrix(y_test, predicted)
print("e. Confusion Metrics: ")
print(conf_metr)