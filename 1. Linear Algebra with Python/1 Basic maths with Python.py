import numpy as np
import sympy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

# Vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.dot(v1,v2))
print("*****")
# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Operations
result = np.dot(A, B)
print(result)
print("*****")
transpose_A = np.transpose(A)
print(transpose_A)
print("*****")

# Matrix Inversion
inverse_A = np.linalg.inv(A)
print(inverse_A)
print("*****")

print("Derivatives for calculas: ") 

# Define symbol
x = sp.Symbol('x')

# Compute derivative
f = x**2 + 3*x + 2
f_prime = sp.diff(f, x)
print(f_prime)
print(f)
print("*****")

print("Probability and Statistics: ")
# Gaussian distribution
mean = 0
std_dev = 1
gaussian_dist = stats.norm(mean, std_dev)

# Generate samples
samples = gaussian_dist.rvs(size=100)

# Calculate mean and variance
mean = np.mean(samples)
variance = np.var(samples)
print("mean: " ,mean)
print("variance: " , variance)
print("*****")

print("Equations and Inequalities: ")
# Solving equations
A = np.array([[2, 3], [1, -2]])
b = np.array([8, 1])
solution = np.linalg.solve(A, b)
print(solution)
print("*****")

print("Function: Linear and Non Linear")

# Linear function
def linear_function(x, m, c):
    return m * x + c

# Non-linear function (e.g., ReLU)
def relu(x):
    return max(0, x)

# Plotting
x_values = np.linspace(-10, 10, 100)
y_values_linear = linear_function(x_values, 2, 3)
y_values_relu = [relu(x) for x in x_values]

plt.plot(x_values, y_values_linear, label='Linear Function')
plt.plot(x_values, y_values_relu, label='ReLU Function')
plt.legend()
plt.show()