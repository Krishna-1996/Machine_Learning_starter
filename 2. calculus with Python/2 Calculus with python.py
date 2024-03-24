import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

'''
# Define a symbol
x = sp.Symbol('x')

# Define a function
def f(x):
    return x**2 + 3*x + 2

# Differentiation using SymPy
f_prime = sp.diff(f(x), x)

# Integration using SymPy
F = sp.integrate(f(x), x)

# Solve equation using SymPy
equation = sp.Eq(f(x), 0)
solution = sp.solve(equation, x)

# Numerical differentiation (using finite differences) with NumPy
def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

x_value = 2
derivative_at_x = numerical_derivative(f, x_value)

# Numerical integration (using NumPy's trapz method for numerical integration)
x_values = np.linspace(0, 1, 100)
y_values = f(x_values)
integral_value = np.trapz(y_values, x=x_values)

# Visualization
plt.figure(figsize=(10, 6))

# Plot the function
plt.plot(x_values, y_values, label='f(x) = x^2 + 3x + 2')

# Plot the derivative
derivative_values = 2*x_values + 3
plt.plot(x_values, derivative_values, label="f'(x) = 2x + 3", linestyle='--')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and its Derivative')
plt.legend()

# Show plot
plt.grid(True)
plt.show()

# Print results
print("Derivative:", f_prime)
print("Indefinite Integral:", F)
print("Solution:", solution)
print("Numerical Derivative at x =", x_value, ":", derivative_at_x)
print("Numerical Integral:", integral_value)
'''

print("***************************************")
print("EXAMPLES with REAL TIME PROBLEMS")
print("***************************************")
# EQUATION 1
# f(x) = x**2 - 4x +4 = 0
print("Equation 1: f(x) = x**2 - 4x +4 = 0")
print("__Solution__")
# Step 1: Define a Symbol
x = sp.symbols('x')
print(x)

# Step 2: Define the Equation
equation = x**2 - 4*x + 4

# Step 3: Solve the Equation
solutions = sp.solve(equation, x)
print("Solutions from Python:", solutions)
