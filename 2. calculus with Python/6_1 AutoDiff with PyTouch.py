# 6_1 AutoDiff with PyTouch.
'''
Equation: 
f(x) y = x^2
dy/dx = 2x = 2(5) = 10
'''
import torch
x = torch.tensor(5.0)
print(x.requires_grad_())#contagiously track gradients through forward pass
y = x**2
y.backward()#use autodifff(dy/dx)
print(x.grad)

#Lets plot the slop as well
import numpy as np
import matplotlib.pylab as plt
#define the function f(x) = x^2:
def f(x):
    return x**2
#Define its derivative dy/dx = 2x:
def df(x):
    return 2*x
#Generate x values:
x_values = np.linspace(-5, 5, 100)

#Calcuate y values for both f(x) and its derivative
y_values_f = f(x_values)
y_values_df = df(x_values)

# Plot the function f(x) = x^2
plt.plot(x_values, y_values_f, label='f(x) = x^2')

# Plot the derivative df/dx = 2x
plt.plot(x_values, y_values_df, label="f'(x) = 2x")

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) = x^2 and its derivative')
plt.legend()

# Show plot
plt.grid(True)
plt.show()