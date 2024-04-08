import torch
import matplotlib.pyplot as plt
import random

#Comment:  Adding and Testing

# Generate an array with 50 score = x values
hours = [random.randint(0, 9) for _ in range(50)]

print(hours)
x_hours = torch.tensor(hours)
print("x_hours: ",x_hours)#x values hours by 50 students
scores = (x_hours**2 + 2*x_hours + 3)
y_score = torch.tensor(scores) + torch.normal(mean= torch.zeros(50), std = 0.2)
print("y_score: ",y_score)

#Lets plot a graph with x and y including 0.2 std noise.
fig, ax = plt.subplot()
plt.title("More hours of study, More score you get")
plt.xlabel("Hours--->")
plt.ylabel("Score--->")
_ = ax.scatter(x_hours, y_score)