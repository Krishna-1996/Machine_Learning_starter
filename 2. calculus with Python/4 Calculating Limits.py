'''Calculating Limits: 

'''


#FOR CONTINIOUS FUNCTION 
#import libraries
import numpy as np
import matplotlib.pyplot as plt
'''
# range for x design a curve
x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
# Plot an equation on y 
y = x**2 + 2*x + 2
#Plot this x, y curve
plt.plot(x, y, label='y=x^2 + 2x + 2')
plt.xlabel('x')#label x
plt.ylabel('y')#label y
plt.title('Plot of y = x^2 + 2x + 2')#title of curve

plt.grid(True)# Add grid

#plt.show()#show  curve
#Zoom untile we get straight line
plt.xlim(-1.01,-0.99)
plt.ylim(0.99,1.01)
plt.show()#show  curve
'''
print("************************************")


#FOR NON-CONTINIOUS FUNCTION 
#Equation 2: lim(x->1){(x**2-1)/(x-1)}
'''
def my_fun(my_x):
        my_y = (my_x**2-1)/(my_x-1)
        return my_y
print(my_fun(2))
print(my_fun(3))
print(my_fun(0.999))#LHS
#my_fun(1) will not executed because 0 can't divide by 0
#makes  this function as non continious
print(my_fun(1.0001))#RHS
#This shows x lim 1 has a answer as y=2 but we cant solve it here. 
#Lets plot this and see the result.
x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
y = (x**2-1)/(x-1)
#Plot this x, y curve
plt.plot(x, y, label='(x**2-1)/(x-1)')
plt.xlabel('x')#label x
plt.ylabel('y')#label y
plt.title('Plot of y = (x**2-1)/(x-1)')#title of curve
plt.axhline(y = 0, color="lightgrey")#plot horizontal line y = 0
plt.axvline(x = 0, color="lightgrey")#plot vertical line x = 0

plt.xlim(-1,5)#x limit
plt.ylim(-1,5)#y limit

plt.axhline(y = 2, color="red", linestyle = '--')#plot horizontal line y = 2
plt.axvline(x = 1, color="red", linestyle = '--')#plot vertical line x = 1
plt.show()#show  curve
'''
print("************************************") 
'''
#Equation 3: lim(x->0){(sin x / x)}
def sin_fun(my_x):
        my_y = np.sin(my_x)/my_x
        return my_y

x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
y = sin_fun(x)

plt.plot(x, y, label='(x**2-1)/(x-1)')
plt.xlabel('x')#label x
plt.ylabel('y')#label y

plt.title('Plot of y = (x**2-1)/(x-1)')#title of curve
plt.axhline(y = 0, color="lightgrey")#plot horizontal line y = 0
plt.axvline(x = 0, color="lightgrey")#plot vertical line x = 0

plt.xlim(-12,12)#x limit
plt.ylim(-2,2)#y limit

plt.axhline(y = 2, color="red", linestyle = '--')#plot horizontal line y = 2
plt.axvline(x = 1, color="red", linestyle = '--')#plot vertical line x = 1
plt.show()#show  curve
'''
print("**********************************") 

#Equation 4: lim(x->infi){25 / x)}

def func(x):
    return 25 / x

# Generate positive and negative x values
x_positive = np.linspace(0.001, 20, 500)  # Generate positive x values from 0.1 to 10
x_negative = np.linspace(-20, -0.001, 500)  # Generate negative x values from -10 to -0.1

# Calculate corresponding y values for positive and negative x
y_positive = func(x_positive)
y_negative = func(x_negative)

# Plot the positive and negative curves
plt.figure(figsize=(8, 6))
plt.plot(x_positive, y_positive, label='$y = \\frac{25}{x}$ for $x > 0$', color='blue')
plt.plot(x_negative, y_negative, label='$y = \\frac{25}{x}$ for $x < 0$', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{25}{x}$')
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.5)  # Vertical line at x=0
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.5)  # Horizontal line at y=0
plt.legend()
plt.grid(True)
plt.ylim(-100, 100)  # Set y-axis limits for better visualization
plt.xlim(-10, 10)    # Set x-axis limits for better visualization
plt.show()