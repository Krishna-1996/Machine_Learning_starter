# 8_3 Advance Partial Derivatives
import numpy as np
#import matplotlib.pyplot as plt
#import torch
import math # for constant pi.

'''
Volume of Cylinder = pi * r^2 * l
We need to find the change in vol w.r.t change in l 
It means we need to know partial derivative of dv/dl

'''
def vol(my_r, my_l):
    return math.pi * my_r**2 * my_l

#Let suppose r = 3 and l = 5
r = torch.tensor(3.0).requires_grad_()
l = torch.tensor(5.0).requires_grad_()
v = vol(r,l)
print("Volume of Cylinder is: ", v)
v.backward
l.grad
print(l)
print(math.pi * 3**2)
v1 = vol(3,6)
v2 = vol(3,7)
v_diff = v2-v1
print(v1, v2)
print(v_diff)

r.grad
'''
dv/dr = 2 * pi *l
'''

delta = 1e-6
print((vol(3+delta,5)-vol(3,5))/delta)
#dividing by delta with restore the scale 









