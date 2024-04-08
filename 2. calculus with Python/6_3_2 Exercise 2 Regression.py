import torch
import matplotlib.pyplot as plt

import random
#Comment:  adding and testing
# Generate an array with 50 score = x values
hours = [random.randint(0, 9) for _ in range(50)]

print(hours)
x_hours = torch.tensor(hours)
print(x_hours)#x values hours by 50 students
scores = (x_hours**2 + 2*x_hours + 3)
y_score = torch.tensor(scores)
