# 5.11 Standardization_Scalar_Pre_Processing_in_Sci-kit_Learn
import pandas as pd
from sklearn.datasets import load_iris
d = load_iris()
df = pd.DataFrame(data = d.data, columns=d.feature_names)
print(df.head())
