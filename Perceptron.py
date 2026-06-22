import numpy as np
import pandas as pd


"""
LOAD DATA FROM EXCEL
"""


df = pd.read_excel("leaves-w-stalks.xlsx")

# Select input columns (features)

X = df[["length", "breadth", "stalk"]].values

y = df["target"].values

# =========================
# SET PARAMETERS
# =========================

learning_rate = 0.01

# How many times the model will go through the whole dataset
epochs = 1000

# Get number of rows and columns in X
n_samples, n_features = X.shape

weights = np.zeros(n_features)
bias = 0

# =========================
# ACTIVATION FUNCTION
# =========================

# This function decides output: 0 or 1
def activation(x):
    # If value is >= 0, output 1 otherwise output 0
    return 1 if x >= 0 else 0

# =========================
# TRAINING FUNCTION
# =========================

def train(X, y):
   
    global weights, bias

    # Repeat learning process many times (epochs)
    for epoch in range(epochs):

        # Loop through each row in the dataset
        for i in range(n_samples):

            # Get one data point (length, breadth, stalk)
            x_i = X[i]

            # Multiply inputs by weights and add bias
            linear_output = np.dot(x_i, weights) + bias

            # Convert result into 0 or 1
            y_pred = activation(linear_output)

            # Calculate error (difference between correct and predicted)
            error = y[i] - y_pred

            # Adjust weights based on error
            weights += learning_rate * error * x_i

            # Adjust bias based on error
            bias += learning_rate * error

# =========================
# PREDICTION FUNCTION
# =========================

def predict(X):
    # List to store predictions
    results = []

    # Loop through each row of input data
    for x_i in X:

        # Calculate weighted sum + bias
        linear_output = np.dot(x_i, weights) + bias

        # Convert to 0 or 1
        y_pred = activation(linear_output)

        # Save prediction
        results.append(y_pred)

    # Return all predictions
    return results

# =========================
# TRAIN THE MODEL
# =========================

# Train the perceptron using Excel data
train(X, y)

# =========================
# TEST THE MODEL
# =========================

# Make predictions using trained model
predictions = predict(X)

# Print predicted values
print("Predictions:", predictions)

# Print actual correct values from dataset
print("Actual:     ", y.tolist())