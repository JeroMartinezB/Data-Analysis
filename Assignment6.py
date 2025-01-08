# Jeronimo Martinez Barragan
# CSC 362
# Assignment 6
# Worked together with Wyatt Walsh on this question

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Normalize data by column
def normalize(df, feature_1):
    df[feature_1] = df[feature_1] / df[feature_1].abs().max()

# Plot the features
def plot(df):
    for column in ["Likes", "Dislikes", "Comments"]:
        normalize(df, column)

    df.plot(kind = 'scatter', x = 'Likes', y = 'Ratings')
    df.plot(kind = 'scatter', x = 'Dislikes', y = 'Ratings')
    df.plot(kind = 'scatter', x  = 'Comments', y = 'Ratings')
    plt.show()


# Open and select the data we want to train the model with
file = pd.read_excel("movies.xlsx")
data_frame = pd.DataFrame(file)
data_frame.dropna(inplace=True)
pd_ratings = data_frame[["Ratings"]]
pd_budget = data_frame[["Budget"]]


# Initialise the parameters
budget = pd_budget.to_numpy()
ratings = pd_ratings.to_numpy()
# Normalize
budget = budget / np.max(np.abs(budget))
ratings = ratings / np.max(np.abs(ratings))

weight = 0.0
bias = 0.0
# Hyperparameter
learning_rate = 0.001

# Gradient descent function
def gradient_descent(x, y, w, b, learning_rate): 
    loss_w = 0.0
    loss_b = 0.0
    N = x.shape[0]

    # loss = (y-(wx+b))**2 
    # Iteratively update the partial derivative for 
    # the w and b
    for xi,yi in zip(x,y):
        loss_w += -2*xi*(yi-(w*xi+b))
        loss_b += -2*(yi-(w*xi+b))
    
    # Update the values and return them
    w = w - learning_rate*(1/N)*loss_w
    b = b - learning_rate*(1/N)*loss_b
    return w, b
    
# Iteratively make updates
for i in range(5000):
    # Run gradient descent
    weight,bias = gradient_descent(budget, ratings, weight, bias, learning_rate)
    # Local variable for the equation y = mx +b
    y = weight*budget + bias
    # Sum of squared error
    loss = np.divide(np.sum((ratings-y)**2, axis =0), budget.shape[0])
    if i%1000 == True:
        print(f'Iteration {i} loss value is {loss}, parameters weight: {weight}, bias: {bias}')
print(f'The optimal gradient value is {weight}, and the optimal intercept value is {bias}')
plot(data_frame)



