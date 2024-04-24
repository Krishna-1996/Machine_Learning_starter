# 8_5 : The Gradient of Cost on Batch of Data 
#Import libraries
import torch
import matplotlib.pyplot as plt

# Define x and y values
xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7])
ys = torch.tensor([-1.9875, -1.7832, -0.0041, 0.00, 0.0100, 0.0341, 1.3453, 2.4353])

#Define regression expression: y = mx + b
def reg(my_x, my_m, my_b):
    return my_x*my_m + my_b

#Define m and b values manually 
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()

#Step 1: Forward Pass
yhat = reg(xs, m, b)
print("yhat: ", yhat)

#Step 2: Compare yhat and actual y values and calculate cost "c".
#We use Mean square error to do this.

def mse(my_yhat, my_y):
    sigma = torch.sum(my_yhat - my_y)**2
    return sigma/len(my_y)

c = mse(yhat, ys)
print("Cost: ", c)

#Step 3: Auto-Diff
c.backward()
print(c)
m.grad
b.grad

#Step 4: 
# partial derivative of cost 'c' w.r.t m 