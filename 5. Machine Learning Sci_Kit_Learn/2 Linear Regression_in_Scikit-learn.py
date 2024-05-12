# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df  = pd.DataFrame(data = iris.data, columns = iris.feature_names)
print(df.head())#print the whole dataset
df.shape
df.plot.scatter(x= 'petal width (cm)', y = 'petal length (cm)', title = 'ScatterPlot')
print(df.corr())
print(df.describe())

