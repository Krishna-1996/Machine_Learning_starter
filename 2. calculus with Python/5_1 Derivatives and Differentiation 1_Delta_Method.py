#Delta Method(∆) is used to find the slope of a curve at any specific point.
'''
dy/dx = lim(∆(x)->0 {(f(x+∆x)-f(x))/∆x}

'''
import numpy as np
import matplotlib.pyplot as plt
#Equation1: y = x**2 + 2*x +2
def fun(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y

x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
y = fun(x)

plt.plot(x, y, label='x**2 + 2*x +2')
plt.xlabel('x')#label x
plt.ylabel('y')#label y
plt.grid(True)
plt.title('Plot of y = x**2 + 2*x +2')#title of curve

#Lets identify the slope where x=2:
#Step 1: Determine the y where x = 2:
p = fun(2)
q = fun(5)

#Step 2: The location of p is (2,10) and q is (5,37)
plt.scatter(2,10)
plt.scatter(5,37)

#Step 3: Find slope m between p and q.
#Find value of m(slope) : m = ∆y/∆x => (y2-y1)/(x2-x1) => (37-10)/(5-2) => 27/3 => 9
m = (37-10)/(5-2)
#Step 4: Plot a line by using : y = mx + b => b = mx-y => 
b = 37 - (m*5)#x1 y1, x2 y2
line_y = (m*x) +b
plt.xlim(-5, 10)
plt.ylim(-5, 150)
plt.plot(x, line_y)
plt.show()