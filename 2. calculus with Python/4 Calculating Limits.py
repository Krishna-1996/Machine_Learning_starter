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
print("**********************************")


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
print("**********************************") 
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

def infi_fun(my_x):
        my_y = 25/my_x
        return my_y
x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
y = infi_fun(x)
plt.plot(x, y, label='25/x')
plt.xlabel('x')#label x
plt.ylabel('y')#label y

plt.title('Plot of y = 25/x')#title of curve

plt.xlim(-10,10)#x limit
plt.ylim(-300,300)#y limit
plt.grid(True)# Add grid

#plt.show()#show  curve
#Here is a gap between two exp, bcuz 25 can't divide by 0.
#Lets seprate this data
right_x = x[x>0]
left_x = x[x<0]
right_y = infi_fun(right_x)
left_y = infi_fun(left_x)

plt.plot(left_x, left_y, c = 'C0')
plt.plot(right_x, right_y, c = 'C0')
plt.xlabel('x')#label x
plt.ylabel('y')#label y

plt.xlim(-10,10)#x limit
plt.ylim(-300,300)#y limit
plt.grid(True)# Add grid

plt.show()#show  curve