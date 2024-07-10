# 5.6 Decision_Tree_in_Scikit_Learn

import pandas as pd
import numpy as np

dataset = pd.read_csv("E:/Machine Learning/Machine Learning/bill_authentication.csv")
print(dataset.shape)
print(dataset.head)

# Adding data 
x = dataset.drop('Class', axis = 1)# x is whole except the class which is target feature of test result 
y = dataset['Class']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# PreProcessing
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print("Confusion_metrics: ", confusion_matrix(y_test, y_pred))
print("classification_report: ", classification_report(y_test, y_pred))

import matplotlib as plt
from sklearn import metrics
cm = metrics.confusion_matrixDisplay