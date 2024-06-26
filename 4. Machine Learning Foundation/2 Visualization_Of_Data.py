# 2 Visualization_Of_Data
#Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#Import csv data file
titanic = pd.read_csv("E:/Machine Learning/Machine Learning/train.csv")
#print(data.head())

#Plot a histogram
plt.hist(titanic['Survived'], bins =2, color='blue')
plt.xlabel('Survived')
plt.ylabel('Frequency')
plt.title('Titanic Survivors')
#plt.show()

#do this with class also

#Co-relation Matrix:  A matrix that shows the relation between multiple parameter and their dependency
import seaborn as sns
numeric_cols = titanic.select_dtypes(include=['float64', 'int64']).columns 
#due to some error need to find the solution 
corr_matrix = titanic[numeric_cols].corr()
#print(corr_matrix)

#add a heatmap in this
plt.figure(figsize = (10,8))
sns.heatmap(corr_matrix, annot= True, cmap = 'coolwarm', fmt = '.2f')
plt.show()
#Done visualization of Dataset with histogram and heatmap



