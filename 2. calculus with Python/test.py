'''
50 students study x hours/day and will score y/100 in the exam. The higher the hours of study, the higher the exam will be. 
The maximum score could be 100. Create a simple ml model with given data with an equation: x^2 +4x +7 = y. 
'''
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data based on the equation: x^2 + 4x + 7 = y
np.random.seed(0)
torch.manual_seed(0)
num_samples = 50
x_values = np.random.uniform(0, 10, num_samples)  # Random hours of study
y_values = x_values ** 2 + 4 * x_values + 7 + np.random.normal(0, 5, num_samples)  # Using the given equation with noise

# Convert data to PyTorch tensors
x_tensor = torch.tensor(x_values, dtype=torch.float32).view(-1, 1)  # Reshape to column vector
y_tensor = torch.tensor(y_values, dtype=torch.float32).view(-1, 1)

# Define a simple neural network model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear1 = nn.Linear(1, 10)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(10, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        return x

# Instantiate the model
model = SimpleModel()

# Define loss function and optimizer
criterion = nn.MSELoss()  # Mean Squared Error loss
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)  # Stochastic Gradient Descent optimizer

# Train the model
num_epochs = 100
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(x_tensor)
    loss = criterion(outputs, y_tensor)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Print progress
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Plot the data and the learned model
plt.scatter(x_values, y_values, label='Original data')
plt.plot(x_values, model(x_tensor).detach().numpy(), color='red', label='Fitted curve')
plt.xlabel('Hours of Study')
plt.ylabel('Exam Score (out of 100)')
plt.title('Simple Machine Learning Model')
plt.legend()
plt.show()
