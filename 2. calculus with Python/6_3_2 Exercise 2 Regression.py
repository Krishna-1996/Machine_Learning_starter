import torch
import matplotlib.pyplot as plt

x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print("x: =",x)

"""The $y$ values were created using the equation of a line $y = mx + b$. This way, we know what the model parameters to be learned are, say, $m = -0.5$ and $b = 2$. Random, normally-distributed noise has been added to simulate sampling error:"""

#y = -0.5*x + 2 + torch.normal(mean=torch.zeros(8), std=0.2)
#y1 = 2**x + 5*x + 7 + torch.normal(mean=torch.zeros(8), std=0.2)
y2 = 2**x + 5*x + 7 + torch.normal(mean=torch.zeros(8), std = 0.4)
y3 = 2**x + 5*x + 7 + torch.normal(mean=torch.absolute(x), std = 0.4)
print("x: ",x)
#print("y: ",y)
#print("y1: ",y1)
print("y2: ",y2)
print("y3: ",y3)
fig, ax = plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (mL)")
plt.ylabel("Forgetfulness")
_ = ax.scatter(x, y2)
plt.show()
fig, ax = plt.subplots()
plt.title("l")
plt.xlabel("Drue (mL)")
plt.ylabel("Fs")
_ = ax.scatter(x, y3)
plt.show()

