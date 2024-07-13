# 5.12 Normalization_Norms_Pre_Processing_in_Sci-kit_Learn

x = [[1,-1,2],
    [4,2,1],
    [0,1,-1]]

from sklearn.preprocessing import normalize
import pandas as pd
import math 

# max-norm
x_norm = normalize(x, norm='max')
print("x_norm: ",x_norm)

x_norm_l1 = normalize(x, norm='l1')
print("x_norm_l1: ",x_norm_l1)

x_norm_l2 = normalize(x, norm='l2')
print("x_norm_l2: ",x_norm_l2)
