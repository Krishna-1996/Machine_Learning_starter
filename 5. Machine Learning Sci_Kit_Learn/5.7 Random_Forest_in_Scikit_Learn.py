# 5.7 Random_Forest_in_Scikit_Learn

from logging import critical
import pandas as pd
import numpy as np
from sympy import ComputationFailed

dataset = pd.read_csv("E:/Machine Learning/Machine Learning/heart.csv")
print(dataset.head(5))

x = dataset.drop('target', axis=1)
y = dataset['target']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0)

# No Pre-Processing
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10, criterion='entropy')
classifier.fit(x_train, y_train)

# Prediction
y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix (y_test, y_pred)
print(" confusion_matrix: ", cm)
accuracy = accuracy_score(y_test, y_pred)
