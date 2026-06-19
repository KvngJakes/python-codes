import pandas as pd
import json
from datetime import datetime


# =====================================
# LOAD DATASET
# =====================================
def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Use .csv or .xlsx"
        )


# =====================================
# STEP ACTIVATION FUNCTION
# =====================================
def step_function(z):
    return 1 if z >= 0 else 0


# =====================================
# CALCULATE ACCURACY
# =====================================
def calculate_accuracy(X, y, weights, bias):

    correct = 0

    for i in range(len(X)):

        z = sum(
            weights[j] * X[i][j]
            for j in range(len(weights))
        ) + bias

        prediction = step_function(z)

        if prediction == y[i]:
            correct += 1

    return (correct / len(y)) * 100


# =====================================
# TRAIN PERCEPTRON
# =====================================
def train_perceptron(df, learning_rate=0.1, epochs=100):

    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    feature_names = list(df.columns[:-1])

    weights = [0.0] * X.shape[1]
    bias = 0.0

    print("\n========== TRAINING START ==========\n")

    for epoch in range(epochs):

        errors = 0

        for i in range(len(X)):

            z = sum(
                weights[j] * X[i][j]
                for j in range(len(weights))
            ) + bias

            prediction = step_function(z)

            error = y[i] - prediction

            if error != 0:
                errors += 1

            # Update weights
            for j in range(len(weights)):
                weights[j] += (
                    learning_rate
                    * error
                    * X[i][j]
                )

            # Update bias
            bias += learning_rate * error

        accuracy = calculate_accuracy(
            X,
            y,
            weights,
            bias
        )

        print(
            f"Epoch {epoch+1:3d} | "
            f"Errors={errors:2d} | "
            f"Accuracy={accuracy:.2f}%"
        )

        # Stop if converged
        if errors == 0:
            print("\nTraining converged.")
            break

    print("\n========== TRAINING COMPLETE ==========")
    print("Weights:", weights)
    print("Bias:", bias)

    return {
        "weights": weights,
        "bias": bias,
        "feature_names": feature_names,
        "accuracy": accuracy,
        "epochs_used": epoch + 1
    }


# =====================================
# SAVE MODEL
# =====================================
def save_model(
    model,
    dataset_name,
    learning_rate,
    filename="perceptron_model.json"
):

    model_data = {
        "model_type": "Perceptron",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "dataset": dataset_name,
        "learning_rate": learning_rate,
        "accuracy": model["accuracy"],
        "epochs_used": model["epochs_used"],
        "feature_names": model["feature_names"],
        "weights": model["weights"],
        "bias": model["bias"]
    }

    with open(filename, "w") as file:
        json.dump(
            model_data,
            file,
            indent=4
        )

    print(
        f"\nModel successfully saved as "
        f"'{filename}'"
    )


# =====================================
# LOAD MODEL
# =====================================
def load_model(filename):

    with open(filename, "r") as file:
        model = json.load(file)

    return model


# =====================================
# MAKE PREDICTION
# =====================================
def predict(sample, model):

    weights = model["weights"]
    bias = model["bias"]

    z = sum(
        weights[i] * sample[i]
        for i in range(len(weights))
    ) + bias

    prediction = step_function(z)

    return prediction


# =====================================
# MAIN PROGRAM
# =====================================
def main():

    print("===== PERCEPTRON TRAINER =====\n")

    file_path = input(
        "Enter dataset path (.csv or .xlsx): "
    )

    learning_rate = float(
        input(
            "Enter learning rate (default 0.1): "
        ) or 0.1
    )

    epochs = int(
        input(
            "Enter number of epochs (default 100): "
        ) or 100
    )

    df = load_data(file_path)

    print("\nDataset Preview:")
    print(df.head())

    model = train_perceptron(
        df,
        learning_rate,
        epochs
    )

    save_model(
        model,
        dataset_name=file_path,
        learning_rate=learning_rate
    )

    print("\n===== TEST PREDICTION =====")

    loaded_model = load_model(
        "perceptron_model.json"
    )

    print(
        "\nFeatures:",
        loaded_model["feature_names"]
    )

    sample = []

    for feature in loaded_model["feature_names"]:

        value = float(
            input(
                f"Enter {feature}: "
            )
        )

        sample.append(value)

    result = predict(
        sample,
        loaded_model
    )

    print(
        "\nPrediction:",
        result
    )

    if result == 1:
        print("Class = Positive")
    else:
        print("Class = Negative")


if __name__ == "__main__":
    main()