import numpy as np
#6.  Norms
'''
In linear algebra, a norm is a function that assigns a strictly positive length or size to each vector in a vector space. It generalizes the notion of the length of a vector in Euclidean space to spaces with any number of dimensions.
'''
norm_vector = np.linalg.norm(vector_row)
print("Norm of vector:", norm_vector)

#7.   Singular Value Decomposition (SVD)
'''
VD is a factorization of a real or complex matrix. For an 
× m × n matrix A, SVD decomposes it into three matrices:
Applications of SVD:
Dimensionality reduction
Data compression
Principal Component Analysis (PCA)
Solving linear least squares problems
'''

# Define a vector
x = np.array([1, 2, 3])

# Calculate L1, L2, and L-Infinity norms
l1_norm = np.linalg.norm(x, ord=1)
l2_norm = np.linalg.norm(x, ord=2)
linf_norm = np.linalg.norm(x, ord=np.inf)

print("L1 Norm:", l1_norm)
print("L2 Norm:", l2_norm)
print("L-Infinity Norm:", linf_norm)

# Define a matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform SVD
U, Sigma, Vt = np.linalg.svd(A)

print("U:", U)
print("Sigma:", Sigma)
print("Vt:", Vt)
