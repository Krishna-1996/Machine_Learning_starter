# Integration using Python Scipy method
# 
from scipy.integrate import quad #"Quadrature = numerical integral"

def g(x):
    return x/2
quad(g,1,2)
