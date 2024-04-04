import numpy as np
import torch

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

# Array operations
array_sum = array_1d + 10
print("\nArray after adding 10 to each element:")
print(array_sum)

# Creating a 1D tensor
tensor_1d = torch.tensor([1, 2, 3, 4, 5])
print("1D Tensor:")
print(tensor_1d)

# Creating a 2D tensor
tensor_2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
print("\n2D Tensor:")
print(tensor_2d)

# Tensor operations
tensor_sum = tensor_1d + 10
print("\nTensor after adding 10 to each element:")
print(tensor_sum)
