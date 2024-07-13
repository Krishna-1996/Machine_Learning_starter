# 5.10 Handling_Numerical_Values_Pre_Processing_in_Sci-kit_Learn

from cv2 import threshold
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
# 5.10.1 Discretization

from sklearn.preprocessing import KBinsDiscretizer
disc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
d = load_iris()
df = pd.DataFrame(data=d.data, columns=d.feature_names)
print(df.head())

disc.fit_transform(df) # This will transform
bins = disc.bin_edges_
print(bins)

# 5.10.2 Binarization
from sklearn.preprocessing import Binarizer
print(df.head())
b = Binarizer(threshold=5)
print(b.fit_transform(df['sepal length (cm)'].values.reshape(-1,1)))
