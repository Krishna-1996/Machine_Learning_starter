# 8_3 Advance Partial Derivatives_Exercise
'''
Partial DErivative for :
z = y^3 + 5xy
'''
import torch 

# dz/dy = 3y^2 + 5 (Change in z w.r.t to change in y value)
def z_wrt_y(my_x, my_y):
    return 3 * my_y**2 + 5 # x is constant here 0



    
