'''Calculus of the Infinitesimals: 
getting slope m on ny curved till its infinity zoom
'''
#import libraries
import numpy as np
import matplotlib.pyplot as plt

# range for x design a curve
x = np.linspace(-10, 10, 1000)#curve start, finish, intervals
# Plot an equation on y 
y = x**2 + 2*x + 2
#Plot this x, y curve
plt.plot(x, y, label='y=x^2 + 2x + 2')
plt.xlabel('x')#label x:
plt.ylabel('x')#label y:
plt.title('Plot of y = x^2 + 2x + 2')#title of curve

plt.grid(True)# Add grid

#plt.show()#show  curve
#Zoom untile we get straight line
plt.xlim(-1.01,-0.99)
plt.ylim(0.99,1.01)
plt.show()#show  curve