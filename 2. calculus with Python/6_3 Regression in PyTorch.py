#6_3 Regression in PyTorch
import torch
import matplotlib.pyplot as plt

# Defines a tensor x containing the dosage levels of a drug for testing disease.
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])

#Equation: y = (m*x) + b
m = -0.5    #Sets the slope of the linear equation y = mx + b.
b = 2       #Sets the y-intercept of the linear equation.
#Due to real world problems, we need to add some noise in this equation by:
y = (m*x) + b + torch.normal(mean=torch.zeros(8), std=0.2)
'''
torch.normal() = Generates random numbers sampled from a normal distribution.
mean=torch.zeros(8) = Sets the mean of the normal distribution to zero for each of the eight elements in the tensor.
std=0.2 = Sets the standard deviation of the normal distribution to 0.2, controlling the amount of noise added to each element.
'''
print(y)
plt.title("Clinical Trial")
plt.xlabel("Drug dosage")
plt.ylabel("Froget fulness")
plt.scatter(x, y)

# Next create slope (line) parameter m with a random pf 0.9...
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()


def regression_plot(my_x, my_y, my_m, my_b):
    plt.scatter(my_x, my_y)
    x_min, x_max = plt.get_xlim()
    y_min, y_max = my_m*x_min + my_b, my_m*my_x + my_b

    plt.set_xlim([x_max,x_max])
    plt.scatter([x_min, x_max], [y_min, y_max])
    plt.show()

regression_plot(x,y,m,b)
'''
def regression_plot(my_x, my_y, my_m, my_b):
    fig, ax = plt.subplots()
    ax.scatter(my_x, my_y)

    x_min, x_max = ax.get_xlim()
    y_min, y_max = my_m * x_min + my_b, my_m * x_max + my_b

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])

    plt.show()

regression_plot(x,y,m,b)


'''