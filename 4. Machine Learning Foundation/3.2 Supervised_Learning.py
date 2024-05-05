# 3.2 SUPERVISED LEARNING
# A==> Single Variant Linear Regression Model:
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
predicted_price_at_1900_area = model.predict(new_area)
print("predicted_price_at_1900_are: = a", predicted_price_at_1900_area)

# B==> Multi Variant Linear Regression Model:
'''
Here we discuss and design a model which reflect the multi variant LRM. 
How multiple parameter effect the prediction value.
'''
from sklearn.model_selection import train_test_split

#for this case extract all the feature except price
features = df.drop('price', axis =1).values
print(column_names)
#Split data into training and testing values
x_train, x_test, y_train, y_test = train_test_split(features, price, test_size=0.2, random_state=42)

#Create and train the LR model
model = LinearRegression()
model.fit(x_train, y_train)

#make prediction
prediction_price = model.predict(x_test)

#Plotting Time
# 1. Scatter Plot
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.scatter(x_test, prediction_price)









