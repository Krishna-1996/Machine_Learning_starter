# 1. Data_Preparation The_Foundation_of_ML

#Import necessary libraries
from re import I
import pandas as pd

#Import csv data file
data = pd.read_csv("E:/Machine Learning/Machine Learning/AB_NYC_2019.csv")
#print(data.head())# give full table 
#print(data.info())# column details 

#Dealing with missing value 
#first check any missing values
missing_values = data.isnull().sum()
print(missing_values)#x column has y missing values

#If we want to remove/ drop any column(here missing values columns)
colm_to_drops = ['id','host_name','last_review','reviews_per_month']
data.drop(colm_to_drops,axis = 1)#Entirely drop the column

# lets suppose we dont want to drop an entire column if it has some missing values.
# So, we use mean/median feature to fill that missing value's space.
data['price'].fillna(data['price'].mean()) #data.['columntofill'].fillnafunction(data.['columntofill'].bymean/median())

#OUTLIERS
'''
Eg: data = 1,4,6,3,8,9,4,6,100,3,2,6,5,8,3,6,1,9,4
here outlier is 100 because it is beyond the average of our dataset 
'''
#Manage outlier (detect and correct them by using python library)

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x = 'price',data=data)
plt.show()

#Some outlier in the price
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3-Q1
print(IQR)



