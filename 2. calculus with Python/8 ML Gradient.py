# 8. ML Gradient:
'''
--> 1. Partial Derivative of Multi variant Function:
--> 2. Partial Derivative Chain Rule:
--> 3. Quadratic Cost:
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
#define function for the Equation:
def func(my_x, my_y):#z = x**2 -y**2
    return my_x**2 - my_y**2 

#define all the x values 1000 from -3 to +3.
xs = np.linspace(-4, 4, 1000)
zs_wrt_xs = func(xs,0)

#Plot the above data:
plt.plot(xs,zs_wrt_xs)
plt.axvline(x=0, color="lightgrey")  # Vertical line at x = 0
plt.axhline(y=0, color="lightgrey")  # Horizontal line at y = 0
plt.xlabel("x values-->")
plt.ylabel("z values-->")
#plt.show()

#Determine the slope:
print("'z' w.r.t 'x'") #dz/dx = 2x
def delz_delx(my_x,my_y):
    return my_x*2 #y = 0(constant)
x_sample = [-3,-2,-1,0,1,2,3]
color = ['red','blue','green','black','green','blue', 'red']

def point_and_tangent_wrt_x(my_xs, my_x, my_y, my_func, fprime, col):
    my_z = my_func(my_x, my_y) #z = f(x,y)
    plt.scatter(my_x, my_z, c =col, zorder =3)

    tangent_m = fprime(my_x,my_y)
    tangent_b = my_z - tangent_m*my_x
    tangent_line = tangent_m*my_xs +tangent_b

    plt.plot(my_xs, tangent_line, c=col, 
             linestyle='dashed', linewidth=0.7, zorder=3)

plt.axvline(x=0, color="lightgrey")  # Vertical line at x = 0
plt.axhline(y=0, color="lightgrey") # Horizontal line at y = 0

for i, x in enumerate(x_sample):
    point_and_tangent_wrt_x(xs, x, 0, func, delz_delx, color[i])

plt.plot(xs, zs_wrt_xs)
plt.ylim(-1,12)
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.show()



























