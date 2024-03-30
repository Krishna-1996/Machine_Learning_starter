# Eigenvalues and Eigenvectors:
'''
Given a square matrix A, an eigenvector v and its corresponding eigenvalue 
λ satisfy the equation:

Av=λv

Here's what Eigenvalues and Eigenvectors represent:

Eigenvectors: These are non-zero vectors that are only scaled by the linear transformation represented by matrix A.
In other words, when the matrix A is applied to an eigenvector, the resulting vector is parallel to the original eigenvector, possibly with a different magnitude.

Eigenvalues: These represent the scaling factor by which the eigenvector is stretched or compressed when the matrix A is applied to it.
'''
import numpy as np

# Define the matrix A
A = np.array([[2, 1],[1, 3]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the results
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
print("*******************")
print("Equation 2")
# Equation 2: 4 X 4 matric
X = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(X)

# Print the results
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)