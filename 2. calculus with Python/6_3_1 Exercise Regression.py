#6_3_1 Exercise 1: Regression in PyTorch
'''
Implement a linear regression model using PyTorch to predict the relationship between hours studied and exam scores. 
Create a synthetic dataset of hours studied and corresponding exam scores. 
Then, train the model using gradient descent to minimize the mean squared error loss.
'''

#Solution:


import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
torch.manual_seed(0)
num_samples = 100
hours_studied = np.random.uniform(0, 10, num_samples)
exam_scores = 2 * hours_studied + np.random.normal(0, 1, num_samples)

# Convert numpy arrays to PyTorch tensors
X = torch.tensor(hours_studied, dtype=torch.float32).reshape(-1, 1)
y = torch.tensor(exam_scores, dtype=torch.float32).reshape(-1, 1)

# Define linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # One input feature and one output

    def forward(self, x):
        return self.linear(x)

# Instantiate the model
model = LinearRegression()

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
num_epochs = 100
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Plot the results
predicted = model(X).detach().numpy()
plt.scatter(hours_studied, exam_scores, label='Original data')
plt.plot(hours_studied, predicted, color='red', label='Fitted line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Linear Regression')
plt.legend()
plt.show()