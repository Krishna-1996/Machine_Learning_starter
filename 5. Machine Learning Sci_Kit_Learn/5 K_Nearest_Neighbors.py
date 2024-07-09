# 5 . K-Nearest Neighbor (KNN)

from sklearn import datasets
import pandas as pd
wine = datasets.load_wine()
df = pd.DataFrame(data = wine.data, columns = wine.feature.names)