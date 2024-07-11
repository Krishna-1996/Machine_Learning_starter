# 5.7 Random_Forest_in_Scikit_Learn

import pandas as pd
import numpy as np

dataset = pd.read_csv("E:/Machine Learning/Machine Learning/heart.csv")
print(dataset.head(5))

x = dataset.drop('target', axis=1)
y = dataset['target']

from sklearn.model_selection