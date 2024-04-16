# 8_2 Calculating Partial Derivatives with PyTorch AutoDiff 
import numpy as np
import matplotlib.pyplot as plt
import torch
import math # for constant pi.

# Define x and y 
x = torch.tensor(0.).requires_grad_()
print("x: ",x)
y = torch.tensor(0.).requires_grad_()
print("y: ",y)

# Given an Equation
print("Equation ==> z = (x^2 - y^2)")

# Define function for the Equation:
def func(my_x, my_y):#z = x**2 -y**2
    return my_x**2 - my_y**2 

z = func(x,y)#z wrt to x and y

z.backward()#AutoDiff

print(z)

x.grad
y.grad
print("x: ",x)
print("y: ",y)