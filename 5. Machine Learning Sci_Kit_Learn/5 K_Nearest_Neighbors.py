# 5 . K-Nearest Neighbor (KNN)

from sklearn import datasets
import pandas as pd

wine = datasets.load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
print(df)

# WITHOUT PRE-PROCESSING
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test  = train_test_split(wine.data, wine.target, test_size=0.3)

# Model for K = 7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

# Check accuracy
from sklearn import metrics
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
# Accuracy:  0.7037037037037037

# WITH PRE-PROCESSING
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
scalar = MinMaxScaler()
scalar.fit(wine.data)
temp = scalar.fit_transform(wine.data)
print(temp[:5])

x_train, x_test, y_train, y_test = train_test_split(temp, wine.target, test_size=0.3)
knn2 = KNeighborsClassifier(n_neighbors=7)
knn2.fit(x_train, y_train)
y_pred2 = knn2.predict(x_test)

# Check accuracy
from sklearn import metrics
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred2))
# Accuracy:  0.9814814814814815