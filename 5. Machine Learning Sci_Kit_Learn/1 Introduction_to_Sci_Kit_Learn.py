from sklearn.datasets import load_iris
iris = load_iris()
col_names = iris.feature_names # type: ignore
target_names = iris.target_names # type: ignore
print("Column names are: ",col_names)
print("Target names are: ", target_names)
