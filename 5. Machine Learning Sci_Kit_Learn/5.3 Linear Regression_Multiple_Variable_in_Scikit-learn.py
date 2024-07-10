# 3. Multiple Variable Linear Regression in Scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data=data.data, columns=data.feature_names)


