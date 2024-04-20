# 8_4 Recap Linear Regression Point by point

import torch
#step 1
# Provide x and y values for calculation 
xs = torch.tensor([1,2,3,4,5,6,7,8,9,10])
ys = torch.tensor([1.344, 2.434, 1.308, 0.554,-1.346, 2.656, 0.244, 0.678, -1.366, -0.244])

#Get slope of line as : y = mx + b
def reg(my_x, my_m, my_b):
    return (my_x*my_m )+ my_b

# Provide m and b value random as 0.9, 0.1 respectively 
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()
# Mark for single instance
i = 7
x = xs[i]
y = ys[i]

yhat = reg(x,m,b)
print(yhat)

# Compare yhat with y to calculate cost "c"
# We use mean square error 
def mn_sq_err(my_yhat, my_y):
    return (my_yhat-my_y)**2

c = mn_sq_err(yhat, y)
print("Cost: ",c)

#Autodiff
c.backward()
m.grad
b.grad
print("Cost: ",c,"m: ", m,"b: ",b)
