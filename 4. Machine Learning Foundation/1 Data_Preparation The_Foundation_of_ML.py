# 1. Data_Preparation The_Foundation_of_ML

#Import necessary libraries
import pandas as pd

#Import csv data file
data = pd.read_csv("E:/Machine Learning/Machine Learning/AB_NYC_2019.csv")
data.head
print(data.info())