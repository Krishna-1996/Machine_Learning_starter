# 5.9 Categorical_Data_ 

import pandas as pd
import numpy as np

x = pd.DataFrame(np.array(['male', 'A+', 'high',
    'female', 'B+', 'medium',
    'male', 'A+', 'low',
    'female', 'B+', 'high',
    'male', 'O+', 'medium',
    'female', 'A+', 'low',
    'male', 'B+', 'high',
    'female', 'A+', 'medium',
    'male', 'B+', 'low',
    'female', 'O+', 'high']).reshape(10, 3))

dx = x

x = pd.DataFrame(x, columns=['gender', 'blood_group', 'edu_Level'])
print("dataFrame: ")
print(x)

from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(dtype='int')
# x['edu_Level'] = encoder.fit_transform(x['edu_Level'].values.reshape(-1, 1))


