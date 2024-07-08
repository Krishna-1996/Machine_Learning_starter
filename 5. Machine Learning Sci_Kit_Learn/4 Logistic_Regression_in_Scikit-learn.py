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
from sklearn.metrics import classification_report, confusion_matrix

# Data
x = np.arange(1000).reshape(-1, 1)
y = np.random.randint(2, size=1000)  # Generating random 0 and 1 for y

# Model
model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict
p_pred = model.predict_proba(x)
y_pred = model.predict(x)
print("Predicted Probabilities:", p_pred)
print("Predicted Classes:", y_pred)

# Score
score = model.score(x, y)
print("Score:", score)

# Confusion Matrix
conf = confusion_matrix(y, y_pred)
print("Confusion Matrix:\n", conf)

# Report
report = classification_report(y, y_pred)
print("Classification Report:\n", report)
