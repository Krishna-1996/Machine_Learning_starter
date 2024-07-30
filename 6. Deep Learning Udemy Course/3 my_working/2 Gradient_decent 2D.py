# 2 Gradient_decent 2D

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# 2D function
def f(x, y):
    return x**2 + y**2

# Gradient of the function
def gradient(x, y):
    return np.array([2 * x, 2 * y])

# Gradient descent function
def gradient_descent_2d(starting_point, learning_rate, n_iterations):
    x, y = starting_point
    trajectory = [(x, y)]
    for _ in range(n_iterations):
        grad = gradient(x, y)
        x, y = x - learning_rate * grad[0], y - learning_rate * grad[1]
        trajectory.append((x, y))
    return np.array(trajectory)

# Parameters
starting_point = (5.0, 5.0)
learning_rate = 0.1
n_iterations = 50

# Perform gradient descent
trajectory = gradient_descent_2d(starting_point, learning_rate, n_iterations)
x_values = np.linspace(-6, 6, 100)
y_values = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = f(X, Y)

# Plot
fig = plt.figure(figsize=(12, 6))

# 3D Surface Plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
ax1.scatter(trajectory[:, 0], trajectory[:, 1], f(trajectory[:, 0], trajectory[:, 1]), color='red', label='Gradient Descent Steps')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')
ax1.set_title('2D Gradient Descent - Surface Plot')

# Contour Plot
ax2 = fig.add_subplot(122)
contour = ax2.contour(X, Y, Z, levels=20, cmap='viridis')
ax2.scatter(trajectory[:, 0], trajectory[:, 1], color='red', label='Gradient Descent Steps')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('2D Gradient Descent - Contour Plot')
ax2.legend()

plt.show()
