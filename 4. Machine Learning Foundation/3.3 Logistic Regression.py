# 3.2 SUPERVISED LEARNING
# Logistic Regression Model:

import numpy as np
# sigmoid function :
def sigmoid(z):
    return 1/(1 + np.exp(-z))


import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("E:/Machine Learning/Machine Learning/Heart_Disease_Data.csv")
print(df.isnull().any())
'''some data has null values . 
so wee need to replace it with the mean value of the dataset and fill it by that mean value'''
df['education'].fillna(df['education'].mean(), inplace=True)
df['cigsPerDay'].fillna(df['cigsPerDay'].mean(), inplace=True)
df['BPMeds'].fillna(df['BPMeds'].mean(), inplace=True)
df['BMI'].fillna(df['BMI'].mean(), inplace=True)
df['heartRate'].fillna(df['heartRate'].mean(), inplace=True)
df['glucose'].fillna(df['glucose'].mean(), inplace=True)
df['totChol'].fillna(df['totChol'].mean(), inplace=True)

#Extract feature and labels from the data
features = df.drop('TenYearCHD', axis =1 ).values
labels = df['TenYearCHD'].values

#Split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42) 

#scale the data if required so that all data will have a common scale
#It will make machine learning to perform coding part easily and fast.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.fit_transform(x_test)

# Create and train the Logistic Regression
model = LogisticRegression()
model.fit(x_train_scaler, y_train)
predicted = model.predict(x_test_scaler)

 #EXTRA
 #plot this data now
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
