# 3. Solving Linear Equations:
# Solving Linear Equations
A = np.array([[2, 3], [4, 5]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print("Solution to Ax = b:")
print(x)