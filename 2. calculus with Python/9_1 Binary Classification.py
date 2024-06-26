# Integration using Python Scipy method:

from scipy.integrate import quad #"Quadrature = numerical integral"

def g(x):
    return x/2
y = quad(g,1,2)
print(y)
'''output would be 0.75 which is = to 3/4'''

#Another example
def a(b):
    return b*2
c = quad(a,3,4)
print(c)