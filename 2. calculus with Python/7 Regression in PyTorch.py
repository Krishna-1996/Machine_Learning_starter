# 6_3 Regression in PyTorch___:
import torch
import matplotlib.pyplot as plt

x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print("x: =",x)

"""The 'y' values were created using the equation of a line $y = mx + b$. This way, we know what the model parameters to be learned are, say, $m = -0.5$ and $b = 2$. Random, normally-distributed noise has been added to simulate sampling error:"""

y = -0.5*x + 2 + torch.normal(mean=torch.zeros(8), std=0.2)

"""For reproducibility of this demo, here's a fixed example of $y$ values obtained by running the commented-out line above:"""

#y = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]) # E.g.: Patient's "forgetfulness score"
print("y: =",y)

fig, ax = plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (mL)")
plt.ylabel("Forgetfulness")
_ = ax.scatter(x, y)

"""Initialize the slope parameter $m$ with a "random" value of 0.9...

(*N.B.*: In this simple demo, we could guess approximately-correct parameter values to start with. 
Or, we could use an algebraic (e.g., Moore-Penrose pseudo-inverse) or statistical (e.g., ordinary-least-squares regression) 
to solve for the parameters quickly. 
This tiny machine learning demo with two parameters and eight data points scales, 
however, to millions of parameters and millions of data points. 
The other approaches -- guessing, algebra, statistics -- do not come close to scaling in this way.)
"""

m = torch.tensor([0.9]).requires_grad_()
print("m: = ",m)

"""...and do the same for the $y$-intercept parameter $b$:"""

b = torch.tensor([0.1]).requires_grad_()
print("b: = ",b)

def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b

def regression_plot(my_x, my_y, my_m, my_b):

    fig, ax = plt.subplots()

    ax.scatter(my_x, my_y)

    x_min, x_max = ax.get_xlim()
    y_min = regression(x_min, my_m, my_b).detach().item()
    y_max = regression(x_max, my_m, my_b).detach().item()

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])

regression_plot(x, y, m, b)
plt.show()
print("Basic done here ")

"""
*Return to slides here if following *Calculus I* class.**

### Machine Learning
In four easy steps :)

*** Step 1*: Forward pass
"""

yhat = regression(x, m, b)
print("yhat: =", yhat)

'''
#**Step 2**: Compare $\hat{y}$ with true $y$ to calculate cost $C$

#There is a PyTorch `MSELoss` method, but let's define it out selves to see how it works. MSE cost is defined by: $$C = \frac{1}{n} \sum_{i=1}^n (\hat{y_i}-y_i)^2 $$
'''

def mse(my_yhat, my_y):
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)

C = mse(yhat, y)
print("Cost: =",C)

"""**Step 3**: Use auto-diff to calculate gradient of $C$ w.r.t. parameters"""

C.backward()

print("m.grad: ",m.grad)

print("b.grad: ",b.grad)

"""**Step 4**: Gradient descent"""

optimizer = torch.optim.SGD([m, b], lr=0.01)
#optimizer with descent gradient = .SGD([list of all para], lr =learning rate(how much change))

optimizer.step()#will adjust the above method

"""Confirm parameters have been adjusted sensibly:"""

print("Will adjust this much m: ",m)
print("Will adjust this much b: ",b)

regression_plot(x, y, m, b)
plt.show()
"""We can repeat steps 1 and 2 to confirm cost has decreased:"""

C = mse(regression(x, m, b), y)#cost after single adjustment
print("New reduce 'Cost' after changing the parameter m and b:")
print("New reduce Cost: =",C)

"""Put the 4 steps in a loop to iteratively minimize cost toward zero:"""

epochs = 1000
for epoch in range(epochs):

    optimizer.zero_grad() # Reset gradients to zero; else they accumulate

    yhat = regression(x, m, b) # Step 1 regression model
    C = mse(yhat, y) # Step 2 calculate cost

    C.backward() # Step 3 backward to 1 and 2 to get new data
    optimizer.step() # Step 4 GD to get slope with adjust to m and b

    print('Epoch {}, cost {}, m grad {}, b grad {}'.format(epoch, '%.3g' % C.item(), '%.3g' % m.grad.item(), '%.3g' % b.grad.item()))

regression_plot(x, y, m, b)
plt.show()

print("Adjusted 'm': = ",m.item())
print("Adjusted 'b': = ",b.item())

"""**N.B.**: The model doesn't perfectly approximate the slope (-0.5) and $y$-intercept (2.0) used to simulate the outcomes $y$ at the top of this notebook. This reflects the imperfectness of the sample of eight data points due to adding random noise during the simulation step. In the real world, the best solution would be to sample additional data points: The more data we sample, the more accurate our estimates of the true underlying parameters will be."""




