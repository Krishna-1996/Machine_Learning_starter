# 2 Visualization_Of_Data
#Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#Import csv data file
data = pd.read_csv("E:/Machine Learning/Machine Learning/train.csv")

#Plot a histogram
plt.hist(data['survived'], bin=2, color='blue')
plt.xlabel('Survived')
plt.ylabel('Frequency')
plt.title('Titanic Survivors')
plt.show()