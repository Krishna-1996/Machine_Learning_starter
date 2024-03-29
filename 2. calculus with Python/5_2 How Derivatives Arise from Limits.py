#How Derivatives arise from limits
#dy/dx = lim(x->x){(f(x+∆x)-f(x))/∆x}
import numpy as np
import matplotlib.pyplot as plt
#function for the equation 
def fun(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y

def diff_demo(my_f, my_x, my_delta):
    return (my_f(my_x + my_delta)-my_f(my_x)) / my_delta

deltas = [1, .01, 0.001, 0.0001, 0.00001, 0.000001]
for delta in deltas:
    print(diff_demo(fun, 2, delta))

for delta in deltas:
    print(diff_demo(fun, -1, delta))
 