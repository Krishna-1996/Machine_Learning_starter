#3.3a Logistic Regression_Churn_Modelling
'''
Is the customer stay with Bank or not ('YES' or 'NO'), and multiple feature is going to effect it.
'''

from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# import dataset of heart_disease 
data = pd.read_csv("E:/Machine Learning/Machine Learning/Churn_Modelling.csv")
print(data)

def signoid(z):
    return 1/(1+np.exp(-z))
# print(data.isnull().any()) #(No required as there is no null value)

# Extract features and labels from data
features = data.drop('Exited', axis=1).values
labels = data['Exited'].values

#Split data for training and testing purpose
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

#Create and train the Logistic Regression




