# 3.2 SUPERVISED LEARNING
# Single Variant Linear Regression Model:
import pandas as pd
df = pd.read_csv("E:/Machine Learning/Machine Learning/house_prices.csv")
# print(df)
column_names = list(df.columns.values)
print(column_names)
# convert the dataset into binary 0 or 1 for better understanding 
#df = pd.get_dummies(df, columns=['mainroad'])