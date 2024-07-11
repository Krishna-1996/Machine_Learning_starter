# 5.7 Random_Forest_in_Scikit_Learn

import pandas as pd
import numpy as np

dataset = pd.read_csv("E:/Machine Learning/Machine Learning/heart.csv")
print(dataset.head(5))

x = dataset.drop('target', axis=1)
y = dataset['target']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0)