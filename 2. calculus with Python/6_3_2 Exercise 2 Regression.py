import random
import torch
import matplotlib.pyplot as plt


#Comment:  Adding and Testing

# Generate an array with 50 score = x values
hours = [random.randint(0, 9) for _ in range(50)]

x_hours = torch.tensor(hours)
#print("x_hours: ",x_hours)#x values hours by 50 students

#scores = (x_hours**2 + 2*x_hours + 3)
y_score = torch.tensor(x_hours**2 + 2*x_hours + 3) + torch.normal(mean= torch.zeros(50), std = 0.2)
#print("y_score: ",y_score)

#Lets plot a graph with x and y including 0.2 std noise.

plt.title("More hours of study, More score you get")
plt.xlabel("Hours--->")
plt.ylabel("Score--->")
plt.scatter(x_hours, y_score)

m = 2
b = 3
#initialize the slope:
def reg(my_x, my_m, my_b):
    return my_m*my_x + my_b

# Plot the slope:
def reg_plot(my_x, my_y, my_m, my_b):
    x_min, x_max = my_x.min().item(), my_x.max().item()
    y_min = reg(x_min, my_m, my_b)
    y_max = reg(x_max, my_m, my_b)
    plt.plot([x_min, x_max], [y_min, y_max], color='red')

reg_plot(x_hours, y_score, m, b)
plt.show()
print("Basic done here ")

    