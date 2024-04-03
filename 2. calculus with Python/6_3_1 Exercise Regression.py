#6_3_1 Exercise 1: Regression in PyTorch
'''
1. Use PyTorch (or TensorFlow, if you like) to find the slope of y=x^{2}+2x+2 where x=2
2. Use the Regression in PyTorch notebook to simulate a new linear relationship between y and x, and then fit the parameters m and b.
'''

#Solution:
#Import libraries:
import torch
import numpy as np
import matplotlib.pyplot as plt

print("Find the slope of x**2 + 2*x + 2, where x = 2")
#Step 1: Define equation in function
def func(x):
    return x**2 + 2*x + 2 

#Step 2: Define x as PyTorch tensor
x = torch.tensor(2.0, requires_grad=True)

#Step 3: Compute the func for y
y = func(x)
print(y)

#Step 4: Compute the gradient (slope of 'y' w.r.t to 'x')
y.backward()

#Step 5: Extract the slope
slope = x.grad.item()
print("The slope of y = x^2 + 2x + 2, where x = 2 is:", slope)





