# Exercise 1: 
# x^2 + 2x +2 = y, where x = 2.and
'''
''' 
#Import libraries:
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

#  find slope
def fun(x):
    return x**2 + 2*x + 2
x = torch.tensor(2.0, requires_grad=True)
print(x)
y = fun(2)
print(y)

























