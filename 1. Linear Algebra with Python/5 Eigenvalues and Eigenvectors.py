# Eigenvalues and Eigenvectors:
'''
Given a square matrix A, an eigenvector v and its corresponding eigenvalue 
λ satisfy the equation:

Av=λv

Here's what eigenvalues and eigenvectors represent:

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