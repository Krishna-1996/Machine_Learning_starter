# 5.8 Handling_Missing_Values_in_Scikit_Learn

import numpy  as np
import pandas as pd

x = pd.DataFrame(np.array([5,3,6,3,np.NaN,np.NaN,np.NaN -2 , 4, 6, np.NaN, 2, 7, 9, np.NaN, 6, np.NaN, 5, np.NaN]).reshape(6,3))
x.columns = ['f1','f2','f3',]
print(x)



