# Delta Method(∆) is used to find the slope of a curve at any specific point.
'''
dy/dx = lim(∆(x)->0 {(f(x+∆x)-f(x))/∆x}

'''
import numpy as np
import matplotlib.pyplot as plt
# Equation1: y = x**2 + 2*x +2
def fun(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y

x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
y = fun(x)
'''
plt.plot(x, y, label='x**2 + 2*x +2')
plt.xlabel('x')#label x
plt.ylabel('y')#label y
plt.grid(True)
plt.title('Plot of y = x**2 + 2*x +2')#title of curve

# Lets identify the slope where x=2:
# Step 1: Determine the y where x = 2:
p = fun(2)#y = 10
q = fun(5)#y = 37
r = fun(2.1)#y = 10.61

print(fun(2))
print(fun(5))
print(fun(2.1))

# Step 2: The location of p is (2,10) and q is (5,37)
plt.scatter(2,10)
plt.scatter(5,37)
plt.scatter(2.1,10.61)

# Step 3: Find slope m between p and q.
#Find value of m(slope) : m = ∆y/∆x => (y2-y1)/(x2-x1) => (37-10)/(5-2) => 27/3 => 9
m = (37-10)/(5-2)
#Step 4: Plot a line by using : y = mx + b => b = mx-y => 
b = 37 - (m*5)#x1 y1, x2 y2
line_y = (m*x) +b
plt.xlim(-5, 10)
plt.ylim(-5, 150)
plt.plot(x, line_y)
plt.show()
print('*************************')
# Plotting then x = 2.1
plt.plot(x, y, label='x**2 + 2*x +2')
plt.xlabel('x')#label x
plt.ylabel('y')#label y
plt.grid(True)
plt.title('Plot of y = x**2 + 2*x +2')#title of curve

# Step 4: The location of p is (2,10) and q is (5,37)
plt.scatter(2,10)
plt.scatter(2.1,10.61)

# Step 5: Find slope m between p and q.
#Find value of m(slope) : m = ∆y/∆x => (y2-y1)/(x2-x1) => (37-10)/(5-2) => 27/3 => 9
m1 = (10.61-10)/(2.1-2)
print("Slop of line is: ",m1)

# Step 4: Plot a line by using : y = mx + b => b = mx-y => 
b = 10.61 - (m1*2.1)#x1 y1, x2 y2
line_y1 = (m1*x) +b
plt.xlim(-5, 10)
plt.ylim(-5, 150)
plt.plot(x, line_y1)
plt.show()'''

#Exercise 1: plot the slope of line point 'p' for x= -1
x1 = 2
y1 = 10
plt.plot(x,y, label='x**2 + 2*x +2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Graph for x = -1')
#Location of p = (2,10)
#Location of p1 = (x1,y1 )
#Step 1: Find the value to y and x = -1
x2 = -1
y2 = fun(x2)
print("y = ", y2)#y = 1
#Location of p1 = (-1,1 )

#Step 2: Plot a location of p and p1
plt.scatter(x1,y1)
plt.scatter(x2,y2)

#Step 3: Find the slope 'm' for line point p and p1
#m = ∆y/∆x = (y2-y1)/(x2-x1)
m = (y2-y1)/(x2-x1)
print("m = ",m)#m = 

#step 4: Plot the line y = m*x + b => p1 = (m*p) + b => b = p1 - (m*p)
b = 1 - (3*-1)
print("b = ",b)# b = 
y2 = (m*x2) + b
plt.xlim(-2, 5)
plt.ylim(-5, 50)
plt.plot(x1, y2)
plt.show()

