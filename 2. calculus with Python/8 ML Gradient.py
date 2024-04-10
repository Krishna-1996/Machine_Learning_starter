# 8. ML Gradient:
'''
--> Partial Derivative of Multi variant Function
--> Partial Derivative Chain Rule
--> Quadratic Cost
--> Gradients
--> Gradient Descent
--> Back-Propagation
'''
# 1. Partial Derivative of Multi variant Function
#Single Regression
'''
z = (x^2 - y^2)
Let's y = zero(constant)
Then, 
==> z = x^2 - 0 #partial derivation of 'z' w.r.t to 'x'.
==> dz/dx = 2x
'''
import numpy as np
import matplotlib.pyplot as plt
import torch
import math # for constant pi.


print("Equation ==> z = (x^2 - y^2)")
#define function for the Equation
def func(my_x, my_y):#z = x**2 -y**2
    return my_x**2 - my_y**2 
#define all the x values 1000 from -3 to +3.
xs = np.linspace(-3, 3, 1000)


























