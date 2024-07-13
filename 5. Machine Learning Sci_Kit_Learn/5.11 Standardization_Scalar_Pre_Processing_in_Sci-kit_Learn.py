# 5.11 Standardization_Scalar_Pre_Processing_in_Sci-kit_Learn
import pandas as pd
from sklearn.datasets import load_iris
d = load_iris()
df = pd.DataFrame(data = d.data, columns=d.feature_names)
print(df.head())

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
print("StandardScaler: ",scale.fit_transform(df['petal length (cm)'].value.reshape(-1,1)))

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler(feature_range=(-3,3))
print("MinMaxScaler: ",scale.fit_transform(df['petal length (cm)'].value.reshape(-1,1)))

from sklearn.preprocessing import MaxAbsScaler
scale = MaxAbsScaler()
print("MaxAbsScaler: ",scale.fit_transform(df['petal length (cm)'].value.reshape(-1,1)))

from sklearn.preprocessing import RobustScaler
scale = RobustScaler(quantile_range=(0.3, 0.7))
print("RobustScaler: ",scale.fit_transform(df['petal length (cm)'].value.reshape(-1,1)))
