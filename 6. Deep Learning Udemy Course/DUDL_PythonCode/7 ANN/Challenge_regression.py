# import libraries
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# ********************************************next
# create data



# ********************************************next
def build_and_train_the_model(x,y):
  
    N = 100
    x = torch.randn(N,1)
    y = x + torch.randn(N,1)/2
 
    # and plot
    plt.plot(x,y,'s')
    plt.show()

        # build model
    ANNreg = nn.Sequential(
        nn.Linear(1,1),  # input layer
        nn.ReLU(),       # activation function
        nn.Linear(1,1)   # output layer
        )
    print(ANNreg)

    # ********************************************next
    # learning rate
    learningRate = .05

    # loss function
    lossfun = nn.MSELoss()

    # optimizer (the flavor of gradient descent to implement)
    optimizer = torch.optim.SGD(ANNreg.parameters(),lr=learningRate)

    # ********************************************next
    # train the model
    numepochs = 500
    losses = torch.zeros(numepochs)


    ## Train the model!
    for epochi in range(numepochs):

    # forward pass
    yHat = ANNreg(x)

    # compute loss
    loss = lossfun(yHat,y)
    losses[epochi] = loss

    # backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step() 

    # ********************************************next

    # show the losses

    # manually compute losses
    # final forward pass
    predictions = ANNreg(x)

    # final loss (MSE)
    testloss = (predictions-y).pow(2).mean()
    print(testloss)
    plt.plot(losses.detach(),'o',markerfacecolor='w',linewidth=.1)
    plt.plot(numepochs,testloss.detach(),'ro')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Final loss = %g' %testloss.item())
    plt.show()

    # ********************************************next
    testloss.item()
    print(testloss.item())
    # ********************************************next
    # plot the data
    plt.plot(x,y,'bo',label='Real data')
    plt.plot(x,predictions.detach(),'rs',label='Predictions')
    plt.title(f'prediction-data r={np.corrcoef(y.T,predictions.detach().T)[0,1]:.2f}')
    plt.legend()
    plt.show()











