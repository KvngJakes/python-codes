import numpy as np
import pandas as pd


"""
LOAD DATA FROM EXCEL
"""


df = pd.read_excel("leaves-w-stalks.xlsx")
df.columns = df.columns.str.strip()

# Select input columns (features)

X = df[["Length", "Breadth", "Stalk"]].values
y = df["Target"].values

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

def activation(x):
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
    results = []
    for x_i in X:
        linear_output = np.dot(x_i, weights) + bias
        y_pred = activation(linear_output)      
        results.append(y_pred)

    # Return all predictions
    return results

# =========================
# TRAIN THE MODEL
# =========================

train(X, y)

# =========================
# SHOW LEARNED WEIGHTS
# =========================

print("\nPERCEPTRON TRAINING RESULTS")
print("=" * 50)

print(f"Weight for Length  : {weights[0]:.4f}")
print(f"Weight for Breadth : {weights[1]:.4f}")
print(f"Weight for Stalk   : {weights[2]:.4f}")
print(f"Bias               : {bias:.4f}")

# =========================
# MAKE PREDICTIONS
# =========================

predictions = predict(X)
predictions = np.array(predictions)

# =========================
# CALCULATE ACCURACY
# =========================

correct = np.sum(predictions == y)
accuracy = (correct / len(y)) * 100

print("\nMODEL PERFORMANCE")
print("=" * 50)
print(f"Correct Predictions : {correct}")
print(f"Total Samples       : {len(y)}")
print(f"Accuracy            : {accuracy:.2f}%")

# =========================
# SHOW ALL RESULTS
# =========================

print("\nDETAILED RESULTS")
print("-" * 70)
print("Sample\tLength\tBreadth\tStalk\tPredicted\tActual")
print("-" * 70)

for i in range(len(y)):
    print(
        f"{i+1}\t"
        f"{X[i][0]:.1f}\t"
        f"{X[i][1]:.1f}\t"
        f"{X[i][2]:.1f}\t"
        f"{predictions[i]}\t\t"
        f"{y[i]}"
    )

predictions = np.array(predictions)

correct = np.sum(predictions == y)

accuracy = correct / len(y)