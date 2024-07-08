# 4 Logistic_Regression_in_Scikit-learn

'''
3 Types of Logistic regression:
1. Binary : Result are 2. 
Eg:  0 or 1, Yes or No. 
2. Nominal : 3+ result and no natural ordering.
Eg: Result for iris classification which has multiple result and there is no natural order.
3. Ordinal : 3+ result and natural ordering.
Eg: Result for which has level as good, better, best. 
'''

# CODING
# Libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Data
x = np.arange(10).reshape(-1,1)
y = np.array([])

# Model
model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x,y)

print(model.intercept_)
print(model.coef_)

# Predict
p_pred = model.predict_proba(x)
y_pred = model.predict(x)
print(p_pred)
print(y_pred)

# Score
score = model.score(x,y)
print(score)

# Confusion_Metrics
conf = 


