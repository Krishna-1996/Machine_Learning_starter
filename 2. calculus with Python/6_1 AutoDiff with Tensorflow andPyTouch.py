import torch
x = torch.tensor(5.0)
x.requires_grad_()#contagiously track gradients through forward pass
y = x**2