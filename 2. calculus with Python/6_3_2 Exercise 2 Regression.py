# 6_3_2 Exercise 2 Regression
# Equation y=x^2 + 3x + 5 where x=4

#Solution:
#Import libraries:
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

'''
Part 1: Find the slope of x**2 + 3*x + 5, where x = 4
'''
print("Find the slope of x**2 + 3*x + 5, where x = 4")
#Step 1: Define equation in function
def func(x):
    return x**2 + 3*x + 5

#Step 2: Define x as PyTorch tensor
x = torch.tensor(2.0, requires_grad=True)

#Step 3: Compute the func for y


#Step 4: Compute the gradient (slope of 'y' w.r.t to 'x')



#Step 5: Extract the slope

print("The slope of y = x^2 + 2x + 2, where x = 2 is:", slope)

'''
Part 2: Using the Regression in PyTorch to simulate a new linear relationship
between y and x, and then fit the parameters m and b with 1000 epochs
'''
# Step1: Generate synthetic data




# Step2: Convert numpy arrays to PyTorch tensors


# Step3: Define linear regression model


# Step4: Instantiate the model


# Step5: Define loss function and optimizer


# Step6: Train the model

    
    # Step8: Backward pass and optimization
   

# Step9: Plot the results



