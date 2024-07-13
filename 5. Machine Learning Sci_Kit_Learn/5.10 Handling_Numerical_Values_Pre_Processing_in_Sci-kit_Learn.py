# 5.10 Handling_Numerical_Values_Pre_Processing_in_Sci-kit_Learn

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
# 5.10.1 Discretization

from sklearn.preprocessing import KBinsDiscretizer
disc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
d = load_iris()
df = pd.DataFrame(data=data, columns=d.features_name)
print(df.head())

# 5.10.2 Binarization