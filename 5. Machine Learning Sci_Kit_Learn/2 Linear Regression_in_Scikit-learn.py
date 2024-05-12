# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn
# 2. Linear Regression in Scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df  = pd.DataFrame(data = iris.data, columns = iris.feature_names)
df.head()#print the whole dataset
df.shape

