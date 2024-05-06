# 4.1 Model _Evaluation_and_Optimization
'''
1. Metrics
2. Cross Validation
3. Over-fitting and Under-fitting
4. Hyper Parameter Tunning
'''

print("Different metrics used in Linear Regression")
import pandas as pd
df = pd.read_csv("E:/Machine Learning/Machine Learning/house_prices.csv")


column_names = list(df.columns.values)

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

'''
Here we discuss and design a model which reflect the multi variant LRM. 
How multiple parameter effect the prediction value.
'''
from sklearn.model_selection import train_test_split

#for this case extract all the feature except price
features = df.drop('price', axis =1).values
#print(column_names)
#Split data into training and testing values
x_train, x_test, y_train, y_test = train_test_split(features, price, test_size=0.2, random_state=42)

#Create and train the LR model
model = LinearRegression()
model.fit(x_train, y_train)

#make prediction
predicted_price = model.predict(x_test)
# print('prediction_price: ',prediction_price)

print("METRICS")
# a. MEAN ABSOLUTE ERROR 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
msa = mean_absolute_error(y_test, predicted_price)
print('a. mean_absolute_error: ',msa)

# b. MEAN SQUARE ERROR
mse = mean_squared_error(y_test, predicted_price)
print('b. mean_squared_error: ',mse)

# c. R2 SCORE
r2 = r2_score(y_test, predicted_price)
print('c. r2_score: ',r2)




