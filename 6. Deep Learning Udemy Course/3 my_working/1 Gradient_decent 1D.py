# 1 Gradient_decent 1D

import numpy as np
import matplotlib.pyplot as plt

# 1D function
def f(x):
    return x**2

# Gradient of the function
def gradient(x):
    return 2 * x

# Gradient descent function
def gradient_descent_1d(starting_point, learning_rate, n_iterations):
    x = starting_point
    trajectory = [x]
    for _ in range(n_iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        trajectory.append(x)
    return trajectory

# Parameters
starting_point = 5.0
learning_rate = 0.1
n_iterations = 20

# Perform gradient descent
trajectory = gradient_descent_1d(starting_point, learning_rate, n_iterations)
x_values = np.linspace(-6, 6, 100)
y_values = f(x_values)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label='f(x) = x^2', color='blue')
plt.scatter(trajectory, [f(x) for x in trajectory], color='red', label='Gradient Descent Steps')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('1D Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()
