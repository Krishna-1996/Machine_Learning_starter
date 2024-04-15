import torch
import matplotlib.pyplot as plt
import random

# Generate an array with 50 score = x values
hours = [random.randint(0, 9) for _ in range(50)]

x_hours = torch.tensor(hours)
original_scores = (x_hours**2 + 2*x_hours + 3)
noisy_scores = original_scores + torch.normal(mean=torch.zeros(50), std=0.2)
m = 2
b = 3
# Plot the scatter plot
plt.title("More hours of study, More score you get")
plt.xlabel("Hours--->")
plt.ylabel("Score--->")
plt.scatter(x_hours, noisy_scores)

# Define the regression function
def reg(my_x, my_m, my_b):
    return my_m * my_x + my_b

# Plot the regression line
def reg_plot(my_x, my_y, my_m, my_b):
    x_min, x_max = my_x.min().item(), my_x.max().item()
    y_min = reg(x_min, my_m, my_b)
    y_max = reg(x_max, my_m, my_b)
    plt.plot([x_min, x_max], [y_min, y_max], color='red')

# Call the reg_plot function to plot the regression line
reg_plot(x_hours, noisy_scores, m, b)

# Show the plot
plt.show()

print("Basic done here ")

print("Hello..!")