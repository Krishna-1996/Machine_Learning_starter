import torch
import matplotlib.pyplot as plt

# Define data points
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])
y = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])

# Define parameters with gradients
m = torch.tensor([0.9], requires_grad=True)
b = torch.tensor([0.1], requires_grad=True)

# Hyperparameters
learning_rate = 0.01
epochs = 1000

# Define loss function (Mean Squared Error)
def mse_loss(y_pred, y_true):
    return torch.mean((y_pred - y_true)**2)

# Define optimizer
optimizer = torch.optim.SGD([m, b], lr=learning_rate)

# Training loop
for epoch in range(epochs):
    # Forward pass
    y_pred = m * x + b
    
    # Calculate loss
    loss = mse_loss(y_pred, y)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    
    # Update parameters
    optimizer.step()

    # Print progress
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Print optimized parameters
print('Optimized parameters:')
print(f'Slope (m): {m.item():.4f}')
print(f'Intercept (b): {b.item():.4f}')

# Plot the data points and the fitted line
plt.scatter(x, y, label='Data Points')
plt.plot(x.detach().numpy(), (m * x + b).detach().numpy(), color='red', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitted Line using PyTorch')
plt.legend()
plt.show()
