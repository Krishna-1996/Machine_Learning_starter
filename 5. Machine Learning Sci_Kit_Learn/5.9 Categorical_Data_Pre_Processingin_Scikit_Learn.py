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

