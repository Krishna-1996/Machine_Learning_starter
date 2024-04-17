# 8_3 Advance Partial Derivatives
import numpy as np
import matplotlib.pyplot as plt
import torch
import math # for constant pi.

'''
Volume of Cylinder = pi * r^2 * l
We need to find the change in vol w.r.t change in l 
It means we need to know partial derivative of dv/dl

'''
def vol(my_r, my_l):
    return math.pi * r**2 * l

#Let suppose r = 3 and l = 5
r = torch.tensor(3.0).requires_grad_()
l = torch.tensor(5.0).requires_grad_()
v = vol(r,l)
print("Volume of Cylinder is: ", v +"m cubic")











