# 5.8 Handling_Missing_Values_in_Scikit_Learn

import numpy  as np
import pandas as pd

x = pd.DataFrame(np.array([5,3,6,3,np.NaN,np.NaN,np.NaN -2 , 4, 6, np.NaN, 2, 7, 9, np.NaN, 6, np.NaN, 5, np.NaN]).reshape(6,3))
x.columns = ['f1','f2','f3',]
print("x_DataFrame: ", x)
print("Number of missing values in total: ",x.isnull().sum().sum()) # number of null values in total

# Handling the missing values by using sklearn
# Indicating or locating the missing values 
from sklearn.impute import MissingIndicator
indicator = MissingIndicator(missing_values=np.NaN)
indicator = indicator.fit_transform(x)
indicator = pd.DataFrame(indicator, columns=['a1','a2','a3',])
print("Indicating the missing_values: ",indicator) # False = Actual number, True = NaN present

# Impute or filling the missing value
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.NaN, strategy = 'mean')
print("New impute Array: ",imp.fit_transform(x))
print("New impute DataFrame: ",pd.DataFrame(imp.fit_transform(x)))



