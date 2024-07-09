# 5 . K-Nearest Neighbor (KNN)

from sklearn import datasets
import pandas as pd

wine = datasets.load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
print(df)

# without pre-processing 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, t_test  = train_test_split(wine.data, wine.target, test_size=0.3)

# Model for K = 7