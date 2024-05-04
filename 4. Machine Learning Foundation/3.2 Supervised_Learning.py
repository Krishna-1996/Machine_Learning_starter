# 3.2 SUPERVISED LEARNING
# Single Variant Linear Regression Model:
import pandas as pd
df = pd.read_csv("E:/Machine Learning/Machine Learning/house_prices.csv")
# print(df) # print the dataset

column_names = list(df.columns.values)
#print(column_names)# print all columns name

# convert the dataset into binary 0 or 1 for better understanding 
df = pd.get_dummies(df, columns=['mainroad'])
df = pd.get_dummies(df, columns=['guestroom'])
df = pd.get_dummies(df, columns=['basement'])
df = pd.get_dummies(df, columns=['hotwaterheating'])
df = pd.get_dummies(df, columns=['airconditioning'])
df = pd.get_dummies(df, columns=['prefarea'])
df = pd.get_dummies(df, columns=['furnishingstatus'])

# lets start with Linear Regression
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



