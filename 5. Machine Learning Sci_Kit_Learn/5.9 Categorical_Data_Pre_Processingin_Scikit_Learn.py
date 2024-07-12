# 5.9 Categorical_Data_Pre_Processing_in_Sci-kit_Learn.py

import pandas as pd
import numpy as np
'''
data = [
    ['male', 'A+', 'high'],
    ['female', 'B+', 'medium'],
    ['male', 'A+', 'low'],
    ['female', 'B+', 'high'],
    ['male', 'O+', 'medium'],
    ['female', 'A+', 'low'],
    ['male', 'B+', 'high'],
    ['female', 'A+', 'medium'],
    ['male', 'B+', 'low'],
    ['female', 'O+', 'high']
]

# Create a NumPy array
arr = np.array(data)

# Define the column names
columns = ['Gender', 'Blood_Group', 'Edu_Level']
df = pd.DataFrame(arr, columns=columns)
print(df)
'''
x = pd.DataFrame(np.array(['male', 'A+', 'high',
    'female', 'B+', 'medium',
    'male', 'A+', 'low',
    'female', 'B+', 'high',
    'male', 'O+', 'medium',
    'female', 'A+', 'low',
    'male', 'B+', 'high',
    'female', 'A+', 'medium',
    'male', 'B+', 'low',
    'female', 'O+', 'high']).reshape(10,3))
dx = x
columns = ['gender', 'blood_group', 'edu_Level']
df = pd.DataFrame(x, columns=columns)
print("dataFrame: ")
print(x)
from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(dtype='int')
x.edu_level = encoder.fit_transform(x.edu_level.values.reshape(-1,1))
