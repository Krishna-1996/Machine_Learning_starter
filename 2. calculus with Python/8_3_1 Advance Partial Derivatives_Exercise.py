# 8_3 Advance Partial Derivatives_Exercise
'''
Partial Derivative Exercise for :
z = y^3 + 5xy
'''
import torch 

# dz/dy = 3y^2 + 5x (Change in z w.r.t to change in y value)
def z_wrt_y(my_x, my_y):
    return 3 * my_y**2 + 5*my_x # x is constant here 0

# Let suppose x = 0 : y = 5
x1 = torch.tensor(0.).requires_grad_()
y1 = torch.tensor(5.).requires_grad_()

z_y = z_wrt_y(x1, y1)
print("Change in z wrt to y :",z_y)
# dz/dx = 5y (Change in z w.r.t to change in x value)
def z_wrt_x(my_x, my_y):
    return 5 *my_y # y is constant here 0

# Let suppose x = 0 : y = 5
x2 = torch.tensor(5.).requires_grad_()
y2 = torch.tensor(0.).requires_grad_()

z_x = z_wrt_x(x2, y2)
print("Change in z wrt to x :",z_x)

    
