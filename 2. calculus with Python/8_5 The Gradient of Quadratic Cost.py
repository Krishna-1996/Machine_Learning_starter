# 8_5 : The Gradient of Quadratic Cost: 

import math 
print("Hello World...Better Luck...!!")
def cal(x, y, z, a, ):
    return ((((x + y)**2 - (z-a)**3) +  ((z-a)**3 - (x + y)**2)) + (x-y+z))/((z*x)+y +a)

result = cal(2,3,4,7)
print(result)