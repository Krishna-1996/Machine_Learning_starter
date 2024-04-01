#6_3 Regression in PyTorch
import torch
import matplotlib.pyplot as plt

# Defines a tensor x containing the dosage levels of a drug for testing disease.
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])

#Equation: y = (m*x) + b
m = -0.5    #Sets the slope of the linear equation y = mx + b.
b = 2       #Sets the y-intercept of the linear equation.
#Due to real world problems, we need to add some noise in this equation by:
y = (m*x) + b + torch.normal(mean=torch.zeros(8), std=0.2)
'''
torch.normal() =  generates random numbers sampled from a normal distribution.
mean=torch.zeros(8) = sets the mean of the normal distribution to zero for each of the eight elements in the tensor.
std=0.2 = sets the standard deviation of the normal distribution to 0.2, controlling the amount of noise added to each element.
'''
print(y)
