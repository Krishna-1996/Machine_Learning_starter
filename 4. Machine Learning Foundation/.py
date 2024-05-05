import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# import dataset of heart_disease 
data = pd.read_csv("E:/Machine Learning/Machine Learning/Churn_Modelling.csv")
print(data)

def sigmoid(z):
    return 1/(1+np.exp(-z))

# Extract features and labels from data
features = data.drop('Exited', axis=1).values
labels = data['Exited'].values

#Split data for training and testing purpose
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

#Create and train the Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)

#Check the accuracy of the model 
accuracy  = accuracy_score(y_test, predicted)
print("Accuracy:", accuracy)
