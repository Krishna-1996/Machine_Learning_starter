# 8_4 Recap Linear Regression Point by point

import torch
#step 1
# Provide x and y values for calculation 
xs = torch.tensor([1,2,3,4,5,6,7,8,9,10])
ys = torch.tensor([1.344, 2.434, 1.308, 0.554,-1.346, 2.656, 0.244, 0.678, -1.366, -0.244])

#Get slope of line as : y = mx + b
def reg(my_x, my_m, my_b):
    return (my_x*my_m )+ my_b


