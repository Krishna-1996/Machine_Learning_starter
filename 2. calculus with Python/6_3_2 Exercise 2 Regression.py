import torch
import matplotlib.pyplot as plt

m = 5.0
m1 = torch.tensor([m]).requires_grad_()
print(m1)
m3 = 10
m2 = torch.tensor([m3*10.0]).requires_grad_()
print(m2)