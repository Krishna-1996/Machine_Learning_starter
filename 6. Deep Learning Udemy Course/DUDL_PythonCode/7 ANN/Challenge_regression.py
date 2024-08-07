# import libraries
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# BUILT AND TRAIN THE MODEL IN ONE FUNCTION
# ********************************************next
def build_and_train_the_model(x,y):
  
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

    return predictions, losses

    # # final loss (MSE)
    # testloss = (predictions-y).pow(2).mean()
    # print(testloss)
    # plt.plot(losses.detach(),'o',markerfacecolor='w',linewidth=.1)
    # plt.plot(numepochs,testloss.detach(),'ro')
    # plt.xlabel('Epoch')
    # plt.ylabel('Loss')
    # plt.title('Final loss = %g' %testloss.item())
    # plt.show()

    # # ********************************************next
    # testloss.item()
    # print(testloss.item())
    # # ********************************************next
    # # plot the data
    # plt.plot(x,y,'bo',label='Real data')
    # plt.plot(x,predictions.detach(),'rs',label='Predictions')
    # plt.title(f'prediction-data r={np.corrcoef(y.T,predictions.detach().T)[0,1]:.2f}')
    # plt.legend()
    # plt.show()


# CREATE DATA FUNCTION.
def create_Data(m):
    # m = slope
    N = 50
    x = torch.randn(N,1)
    y = x + torch.randn(N,1)/2
    return x, y

# TEST IT ONCE
# create a dataset
x,y = create_Data(.8)

# run the model
yHat,losses = build_and_train_the_model(x,y)
yHat = yHat.detach()

fig,ax = plt.subplots(1,2,figsize=(12,4))

ax[0].plot(losses.detach(),'o',markerfacecolor='w',linewidth=.1)
ax[0].set_xlabel('Epoch')
ax[0].set_title('Loss')

ax[1].plot(x,y,'bo',label='Real data')
ax[1].plot(x,yHat,'rs',label='Predictions')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_title(f'prediction-data corr = {np.corrcoef(y.T,yHat.T)[0,1]:.2f}')
ax[1].legend()

plt.show()

# NOW THE EXPERIMENT TIME
# (takes 3 mins with 21 slopes and 50 exps)

# the slopes to simulate
slopes = np.linspace(-2,2,21)

numExps = 50

# initialize output matrix
results = np.zeros((len(slopes),numExps,2))

for slopei in range(len(slopes)):

  for N in range(numExps):

    # create a dataset and run the model
    x,y = create_Data(slopes[slopei])
    yHat,losses = build_and_train_the_model(x,y)
    yHat = yHat.detach()

    # store the final loss and performance
    results[slopei,N,0] = losses[-1]
    results[slopei,N,1] = np.corrcoef(y.T,yHat.T)[0,1]


# correlation can be 0 if the model didn't do well. Set nan's->0
results[np.isnan(results)] = 0

# PLOT THE RESULT
# plot the results!

fig,ax = plt.subplots(1,2,figsize=(12,4))

ax[0].plot(slopes,np.mean(results[:,:,0],axis=1),'ko-',markerfacecolor='w',markersize=10)
ax[0].set_xlabel('Slope')
ax[0].set_title('Loss')

ax[1].plot(slopes,np.mean(results[:,:,1],axis=1),'ms-',markerfacecolor='w',markersize=10)
ax[1].set_xlabel('Slope')
ax[1].set_ylabel('Real-predicted correlation')
ax[1].set_title('Model performance')

plt.show()



