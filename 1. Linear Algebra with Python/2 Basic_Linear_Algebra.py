import numpy as np
# 1. Scalars, Vectors, and Matrices:
# # Scalars
scalar = 5
print("Scalar: is a single numerical value", scalar)

# Vectors
vector_row = np.array([1, 2, 3])  # Row vector
vector_column = np.array([[1], [2], [3]])  # Column vector
print("Vector: A vector is an array of numbers.")
print("Row vector:", vector_row)
print("Column vector:", vector_column)

# Matrices
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix: A matrix is a 2D array of numbers.")
print(matrix)

# 2. Basic Operations:

# Matrix Addition and Subtraction
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C_addition = A + B
C_subtraction = A - B
print("Matrix Addition:")
print(C_addition)
print("Matrix Subtraction:")
print(C_subtraction)

# Scalar Multiplication
scalar = 2
C_scalar_multiplication = scalar * A
print("Scalar Multiplication:")
print(C_scalar_multiplication)

# Matrix Multiplication
D = np.array([[1, 2, 3], [4, 5, 6]])
E = np.array([[7, 8], [9, 10], [11, 12]])
F = np.dot(D, E)
print("Matrix Multiplication:")
print(F)

# Transpose
G = np.array([[1, 2], [3, 4], [5, 6]])
G_transpose = np.transpose(G)
print("Transpose: Row to Column or visa-versa")
print(G_transpose)

# 3. Matrics Operations: