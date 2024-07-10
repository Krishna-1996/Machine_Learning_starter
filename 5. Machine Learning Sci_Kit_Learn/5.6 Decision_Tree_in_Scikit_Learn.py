# 5.6 Decision_Tree_in_Scikit_Learn

import pandas as pd
import numpy as np

dataset = pd.read_csv("E:/Machine Learning/Machine Learning/bill_authentication.csv")
print(dataset.shape)
print(dataset.head)

# Adding data 
x = dataset.drop('Class', axis = 1)# x is whole except the class which is target feature of test result 
y = dataset['Class']
