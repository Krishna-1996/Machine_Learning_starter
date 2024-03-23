# 3. Solving Linear Equations:
# Solving Linear Equations
import numpy as np
#Equation 1
# Step 1: Formulate the system of linear equations
A = np.array([[2, 3], [4, 5]])
b = np.array([5, 6])
# Step 2: Solve for x
x = np.linalg.solve(A, b)
# Step 3: Print the solution
print("Solution to Ax = b:")
print(x)
print("*******************")
#Equation 2
m = np.array([[2, 3], [5, -1]])
n = np.array([8, -2])
p = np.linalg.solve(m, n)
print("Solution to mp = n:")
print(p)
print("*******************")
#Equation 3
A = np.array([[7, 2], [-14, 0]])
b = np.array([8, 0])

x = np.linalg.solve(A, b)
print("Solution to Ax = b:")
print("Solution: x =", x)

#Equation 4
'''
    2x+3y−z=10
    4x−y+2z=5
    x−2y+3z=−1

'''
i = np.array([[2, 3, -1], [4, -1, 2], [1, -2, 3]])
j = np.array([10, 5 ,-1])

k = np.linalg.solve(i, j)
print("Solution to ik = j:")
print(k)

#Equation 5
'''
    x+2y+3z=6
    2x−y+2z=7
    3x+3y−z=8
​
'''

E = np.array([[1, 2, 3],[2, -1, 2],[3, 3, -1],])
f = np.array([6, 7, 8])

g = np.linalg.solve(E, f)
print("SOlution for Eg = f: ")
print(g)