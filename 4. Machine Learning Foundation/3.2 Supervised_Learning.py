# 3.2 SUPERVISED LEARNING
# Single Variant Linear Regression Model:
import pandas as pd
df = pd.read_csv("E:/Machine Learning/Machine Learning/house_prices.csv")
# print(df) # print the dataset

column_names = list(df.columns.values)
print(column_names)# print all columns name

# convert the dataset into binary 0 or 1 for better understanding 
df = pd.get_dummies(df, columns=['mainroad'])
df = pd.get_dummies(df, columns=['guestroom'])
df = pd.get_dummies(df, columns=['basement'])
df = pd.get_dummies(df, columns=['hotwaterheating'])
df = pd.get_dummies(df, columns=['airconditioning'])
df = pd.get_dummies(df, columns=['prefarea'])
df = pd.get_dummies(df, columns=['furnishingstatus'])

# lets start with Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

'''
we need 2 parameters for single LR, as 'x' and 'y'. So here we use, area and price with relation of:
How much price 'x' would be if the area is 'y'....?
'''
#extract area as sq_foot and price as prices from dataset
area = df['area'].values
price = df['price'].values

#reshare the data for 1 Dimension 
x = area.reshape(-1,1) # type: ignore

#Create and train the LR model
model = LinearRegression()
model.fit(x, price) # type: ignore

#predict the price as according to the given area.Eg: 1900
new_area = np.array([[1900]])
predicted_price = model.predict(new_area)
print(predicted_price)






