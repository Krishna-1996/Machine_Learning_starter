# 6_3_2 Exercise 2 Regression
# Equation y=x^2 + 3x + 5 where x=4

#Solution:
#Import libraries:
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

'''
Part 1: Find the slope of x**2 + 2*x + 2, where x = 2
'''
print("Find the slope of x**2 + 2*x + 2, where x = 2")
#Step 1: Define equation in function


#Step 2: Define x as PyTorch tensor

#Step 3: Compute the func for y


#Step 4: Compute the gradient (slope of 'y' w.r.t to 'x')



#Step 5: Extract the slope

print("The slope of y = x^2 + 2x + 2, where x = 2 is:", slope)

'''
Part 2: Using the Regression in PyTorch to simulate a new linear relationship
between y and x, and then fit the parameters m and b with 1000 epochs
'''
# Step1: Generate synthetic data


x = np.random.uniform(0,10,num_samples)
y = 2 * x + np.random.normal(0,1,num_samples)

# Step2: Convert numpy arrays to PyTorch tensors
X = torch.tensor(x, dtype=torch.float32).reshape(-1, 1) # torch.tensor= convert np array to torch tensor
Y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

# Step3: Define linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # One input feature and one output

    def forward(self, x):
        return self.linear(x)

# Step4: Instantiate the model
model = LinearRegression()

# Step5: Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Step6: Train the model
num_epochs = 1000
for epoch in range(num_epochs):
    # Step7: Forward pass
    outputs = model(X)
    loss = criterion(outputs, Y)
    
    # Step8: Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step9: Plot the results
predicted = model(X).detach().numpy()
plt.scatter(x, y, label='Original data')
plt.plot(x, predicted, color='red', label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()


